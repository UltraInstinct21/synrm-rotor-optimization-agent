"""Tests for the wiki agent tool."""

import json
from src.tools.wiki import wiki_tool


def test_wiki_tool_list():
    res = wiki_tool.invoke({"action": "list"})
    data = json.loads(res)
    assert data["status"] == "success"
    assert "wiki_pages" in data
    assert isinstance(data["wiki_pages"], list)


def test_wiki_tool_read_write_search():
    # Write a test page
    write_res = wiki_tool.invoke({
        "action": "write",
        "page_path": "test_temp_page.md",
        "content": "# Test Wiki Page\nThis is a test wiki document for DeepAgent tests."
    })
    w_data = json.loads(write_res)
    assert w_data["status"] == "success"

    # Search for it
    search_res = wiki_tool.invoke({"action": "search", "query": "test wiki document"})
    s_data = json.loads(search_res)
    assert s_data["status"] == "success"
    assert len(s_data["matches"]) > 0

    # Read it
    read_res = wiki_tool.invoke({"action": "read", "page_path": "test_temp_page.md"})
    r_data = json.loads(read_res)
    assert r_data["status"] == "success"
    assert "Test Wiki Page" in r_data["content"]
