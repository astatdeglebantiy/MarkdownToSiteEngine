---
title: Welcome
---

# Home Page

Welcome to your standalone Markdown website engine.

## Navigation
* [Example Page](example) `example`
* [Example Subpage Directly](example/subpage) `example/subpage`
* [Raw Example](/raw/example) `/raw/example`
* [Raw Example Subpage Directly](/raw/example/subpage) `/raw/example/subpage`

## Resources
* [Sample (raw)](/resources/sample.txt) `/resources/sample.txt`

---

@posts_list(posts)

---

<div class="info-card">
  This is a raw HTML element with custom styles.
</div>

<style>
  .info-card {
    background: #82bdff;
    border: 1px solid #374151;
    padding: 15px;
    border-radius: 6px;
    margin: 20px 0;
  }
  .info-card p {
    margin: 0;
    color: #000000;
  }
</style>