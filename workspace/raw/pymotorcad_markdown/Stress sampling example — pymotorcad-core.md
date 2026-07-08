![](_page_0_Picture_2.jpeg)

Note

Go to the end to download the full example code.

### Stress sampling example

This example shows how to sample the stresses in the rotor bridges.

In addition to calculating the average rotor bridge stress, it also allows post-processing to consider non-linear plastic effects. Optionally, the results from the non-linear calculation are used to replace the standard result in the outputs tab.

This script should be run from the scripting tab after the stress calculation has been run in Motor-CAD.

#### Standard imports

```
import math
import os
import sys
import numpy as np
import ansys.motorcad.core as pymotorcad
```

# Utility functions to check non-linear material data

```
def check_youngs_modulus(non_linear_strain, non_linear_stress, youngs_modulus):
    """Check the initial slope of the non-linear stress strain curve matches the Young
    Parameters
    ----------
    non_linear_strain : list or ndarray
        Strain values
    non_linear_stress : list or ndarray
        Corresponding stress values in MPa
    youngs_modulus : float
        Young's modulus in MPa
    Returns
    -------
    None
    Raises
    ------
    ValueError
        If the initial slope is not consistent with the Young's modulus.
    """
    initial_youngs_modulus = (non_linear_stress[1] - non_linear_stress[0]) / (
        non_linear_strain[1] - non_linear_strain[0]
    )
    # Error if notably different
    if not math.isclose(initial_youngs_modulus, youngs_modulus, rel_tol=0.01, abs_tol=
        raise ValueError(
            "Youngs Modulus and initial slope of non-linear data are different, "
            "please check the inputs. Initial slope is "
            + str(initial_youngs_modulus)
            + " MPa "
            + "Young's modulus is "
            + str(youngs_modulus)
            + " MPa"
        )
def find_divergence_point(non_linear_strain, non_linear_stress, youngs_modulus):
    """Find last point where the non-linear stress strain curve is on the linear region
    Parameters
    ----------
    non_linear_strain : list or ndarray
        Strain values
    non_linear_stress : list or ndarray
        Corresponding stress values in MPa
    youngs_modulus : float
        Young's modulus in MPa
    Returns
    -------
    float
        The last stress point in the linear range
    """
    for i in range(1, len(non_linear_stress)):
        if not math.isclose(
            non_linear_stress[i] / non_linear_strain[i], youngs_modulus, rel_tol=0.000
        ):
            return non_linear_stress[i - 1]
    # Return maximum stress in list if no divergence found
    return non_linear_stress[-1]
```

#### Functions to estimate plastic results

```
def apply_neuber_correction(elastic_stress, youngs_modulus, non_linear_strain, non_linear_str
    """Update the Neuber correction estimates from the Von Mises stress.
    Parameters
    ----------
    elastic_stress : float
        The linear stress input
    youngs_modulus : float
        The Young's modulus used in the linear stress calculation.
    non_linear_strain, non_linear_stress : np.ndarray
        Corresponding arrays of strain (ratio) and stress (MPa) for the non-linear cor
    """
    elastic_strain = elastic_stress / youngs_modulus
    elastic_stress_strain_product = elastic_stress * elastic_strain
    # Check input data is sensible
    check_youngs_modulus(non_linear_strain, non_linear_stress, youngs_modulus)
    # If on the elastic portion, just return inputs, so we don't get interpolation erro
    if elastic_stress < find_divergence_point(non_linear_strain, non_linear_stress, yo
        return {
            "nonlinear_strain": elastic_strain,
            "nonlinear_stress": elastic_stress,
            "plastic_strain": 0,
        }
    # Find a matching stress-strain product in the non-linear response
    # (This is the Neuber correction)
    non_linear_stress_strain_product = non_linear_stress * non_linear_strain
    # Error if out of range:
    if elastic_stress_strain_product > np.max(non_linear_stress_strain_product):
        raise ValueError(
            "Input too large (elastic stress strain product > maximum stress strain pro
            "non-linear data). "
            "Elastic stress is "
            + str(elastic_stress)
            + ", elastic stress strain product is "
            + str(elastic_stress_strain_product)
            + ", maximum plastic stress strain product is "
            + str(np.max(non_linear_stress_strain_product))
        )
    # Lookup to find non-linear strain at matching stress strain product:
    equivalent_non_linear_strain = np.interp(
        elastic_stress_strain_product, non_linear_stress_strain_product, non_linear_st
    )
    # Lookup to find non-linear stress at this strain:
    equivalent_non_linear_stress = np.interp(
        equivalent_non_linear_strain, non_linear_strain, non_linear_stress
    )
    # Find plastic strain
    plastic_strain = equivalent_non_linear_strain - elastic_strain
    return {
        "nonlinear_strain": float(equivalent_non_linear_strain),
        "nonlinear_stress": float(equivalent_non_linear_stress),
        "plastic_strain": float(plastic_strain),
    }
def apply_glinka_correction(elastic_stress, youngs_modulus, non_linear_strain, non_linear_str
    """Update the Glinka correction estimates from the Von Mises stress.
```

*Parameters*

```
----------
elastic_stress : float
    The linear stress input
youngs_modulus : float
    The Young's modulus used in the linear stress calculation.
non_linear_strain, non_linear_stress : np.ndarray
    Corresponding arrays of strain (ratio) and stress (MPa) for the non-linear cor
"""
elastic_strain = elastic_stress / youngs_modulus
elastic_stress_strain_integral = 0.5 * elastic_strain * elastic_stress
# Check input data is sensible
check_youngs_modulus(non_linear_strain, non_linear_stress, youngs_modulus)
# If on the elastic portion, just return inputs, so we don't get interpolation erro
if elastic_stress < find_divergence_point(non_linear_strain, non_linear_stress, yo
    return {
        "nonlinear_strain": elastic_strain,
        "nonlinear_stress": elastic_stress,
        "plastic_strain": 0,
    }
# Find a matching stress-strain integral in the non-linear response
# (This is the Glinka correction)
non_linear_stress_strain_integral = np.zeros(len(non_linear_stress))
for i in range(1, len(non_linear_stress)):
    # This assumes that our stress strain curve starts at zero,
    # and uses simple trapezium integration
    non_linear_stress_strain_integral[i] = (
        non_linear_stress_strain_integral[i - 1]
        + (non_linear_strain[i] - non_linear_strain[i - 1])
        * (non_linear_stress[i] + non_linear_stress[i - 1])
        / 2
    )
# Error if out of range:
if elastic_stress_strain_integral > np.max(non_linear_stress_strain_integral):
    raise ValueError(
        "Input too large (elastic stress strain integral > "
        "maximum stress strain integral in non-linear data). "
        "Elastic stress is "
        + str(elastic_stress)
        + ", elastic stress strain integral is "
        + str(elastic_stress_strain_integral)
        + ", maximum plastic stress strain integral is "
        + str(np.max(non_linear_stress_strain_integral))
    )
# Lookup to find non-linear strain at matching stress strain integral:
equivalent_non_linear_strain = np.interp(
    elastic_stress_strain_integral, non_linear_stress_strain_integral, non_linear_
)
# Lookup to find non-linear stress at this strain:
equivalent_non_linear_stress = np.interp(
    equivalent_non_linear_strain, non_linear_strain, non_linear_stress
)
# Find plastic strain
plastic_strain = equivalent_non_linear_strain - elastic_strain
return {
    "nonlinear_strain": float(equivalent_non_linear_strain),
    "nonlinear_stress": float(equivalent_non_linear_stress),
```

"plastic\_strain": float(plastic\_strain), }

#### Functions to find stress sample points for average stresses

```
def find_bridge_stress_sample_points(mc):
    all_points = []
    # Sample points is hardcoded to 15 in Motor-CAD for stress averaging
    sample_points = 15
    # Check the rotor type
    rotor_type = mc.get_variable("BPMRotor")
    # U shape is 13, V web is 11
    if rotor_type == 11:
        layers = mc.get_variable("VMagnet_Layers")
    elif rotor_type == 13:
        layers = mc.get_variable("Magnet_Layers")
    else:
        sys.exit("Stress sampling only available for V web and U templates")
    # Get variables independent of the rotor type
    average_stress_location_bridge = mc.get_variable("AvStressRadialLocation_Bridge")
    rotor_diameter = mc.get_variable("RotorDiameter")
    poles = mc.get_variable("Pole_Number")
    pole_pairs = poles / 2
    for layer in range(layers):
        if rotor_type == 11:
            # V Web template
            bridge_thickness = mc.get_array_variable("BridgeThickness_Array", layer)
            web_thickness = mc.get_array_variable("WebThickness_Array", layer)
            pole_arc = math.radians(mc.get_array_variable("PoleArc_Array", layer) / po
            theta_4 = math.asin(web_thickness / (2 * (rotor_diameter / 2 - bridge_thic
            theta_0 = math.radians(180 / poles) + pole_arc / 2
            theta_1 = math.radians(360 / poles) - theta_4
            theta_bridge_span = theta_1 - theta_0
            # Arc covers half the bridge
            delta_theta = theta_bridge_span / 2 / sample_points
            theta = theta_0 + theta_bridge_span / 2
        elif rotor_type == 13:
            # U template
            bridge_thickness = mc.get_array_variable("UShape_BridgeThickness_Array", l
            web_thickness = mc.get_array_variable("UShape_WebThickness_Array", layer)
            outer_thickness = mc.get_array_variable("UShape_Thickness_Outer_Array", lay
            theta_offset = math.radians(
                mc.get_array_variable("UShape_OuterAngleOffset_Array", layer)
            )
            inner_rad = rotor_diameter / 2 - bridge_thickness
            # The start angle of the FEA model
            theta_0 = math.radians(360 / poles)
            # The angle to the end of the web
            theta_1 = math.asin(web_thickness / (2 * inner_rad))
            # We now need to solve for phi (the arc angle from the centre) with
            # cos(theta_offset - theta_1 - phi/2) * sin(phi/2) = outer_thickness / (2
            # This is non-trivial, so do this numerically
            test_phi = 0
            found_phi = False
            phi_step = math.radians(0.01)
            iteration = 0
            last_err = math.cos(theta_offset - theta_1 - test_phi / 2) * math.sin(
                test_phi / 2
            ) - outer_thickness / (2 * inner_rad)
            while found_phi == False and iteration < 36000:
                test_phi = test_phi + phi_step
                iteration = iteration + 1
                err = math.cos(theta_offset - theta_1 - test_phi / 2) * math.sin(
```

```
test_phi / 2
            ) - outer_thickness / (2 * inner_rad)
            # Check if error has changed sign, if so we are close to the correct so
            if err * last_err < 0:
                found_phi = True
            else:
                last_err = err
        theta_bridge_span = test_phi
        # Arc covers half the bridge
        delta_theta = theta_bridge_span / 2 / sample_points
        theta = theta_0 - (theta_1 + theta_bridge_span / 2)
    # Common logic for both rotor types
    r0 = rotor_diameter / 2 - bridge_thickness * (1 - average_stress_location_brid
    layer_points = []
    for point in range(sample_points):
        this_theta = theta + point * delta_theta
        x = r0 * math.cos(this_theta)
        y = r0 * math.sin(this_theta)
        layer_points.append([x, y])
    all_points.append(layer_points)
return all_points
```

## Non-linear stress strain data for rotor material

Our non-linear stress-strain data, in this case for a region with Young's modulus of 185 GPa, and with plastic deformation above 480 MPa. Strain is a ratio (dimensionless), Stress is in MPa.

```
non_linear_strain = np.array(
    [
        0,
        0.0002,
        0 0004
```

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026