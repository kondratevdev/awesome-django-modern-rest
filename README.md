# Awesome Django Modern REST [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

<div align="center">
  <img src="https://raw.githubusercontent.com/kondratevdev/awesome-django-modern-rest/master/assets/logo-dark.svg#gh-light-mode-only" alt="Awesome Modern REST Logo - Light" width="100%" height="auto" />
  <img src="https://raw.githubusercontent.com/kondratevdev/awesome-django-modern-rest/master/assets/logo-light.svg#gh-dark-mode-only" alt="Awesome Modern REST Logo - Dark" width="100%" height="auto" />

<!--lint disable double-link-->
[![CI](https://github.com/kondratevdev/awesome-django-modern-rest/actions/workflows/ci.yml/badge.svg)](https://github.com/kondratevdev/awesome-django-modern-rest/actions/workflows/ci.yml)
[![Modern REST](https://img.shields.io/badge/Modern%20REST-0C4B33?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA4MCIgaGVpZ2h0PSIxMDgwIiB2aWV3Qm94PSIwIDAgMTA4MCAxMDgwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cGF0aCBkPSJNMiA3MDQuMDJMMTQ1LjQ1OSA0NjYuMTlMMjc3Ljg4MyA3MDQuMDJMMTQ1LjQ1OSA5NDEuODQ5TDIgNzA0LjAyWiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTE0NS40NTkgOTQxLjg0OUwyIDcwNC4wMkgyNzcuODgzTDE0NS40NTkgOTQxLjg0OVoiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik02NzguOTQ4IDcwNC4wMzVMMzQxLjIzIDEzOEwyMjcuMDcxIDMyOC4yNjRMNDM2LjM2MiA3MDQuMDM1TDMwMy4xNzcgOTQxLjg2NEg1MzYuMjVMNjc4Ljk0OCA3MDQuMDM1WiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTY3OC45MzcgNzA0LjAyNkg0MzYuMzVMMzAzLjE2NiA5NDEuODU2SDUzNi4yMzlMNjc4LjkzNyA3MDQuMDI2WiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTEwNzguMTcgNzA0LjAzNUw3NDAuNDUxIDEzOEw2MjYuMjkzIDMyOC4yNjRMODM1LjU4MyA3MDQuMDM1TDcwMi4zOTkgOTQxLjg2NEg5MzUuNDcyTDEwNzguMTcgNzA0LjAzNVoiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik0xMDc4LjE3IDcwNC4wMzVIODM1LjU4M0w3MDIuMzk5IDk0MS44NjRIOTM1LjQ3MkwxMDc4LjE3IDcwNC4wMzVaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K&color=35544A)](https://github.com/wemake-services/django-modern-rest)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/django-modern-rest?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=BRIGHTGREEN&left_text=downloads)](https://pepy.tech/projects/django-modern-rest)
[![Telegram chat](https://img.shields.io/badge/chat-join-blue.svg?logo=telegram)](https://t.me/django_modern_rest)

> A curated list of resources related to Django Modern REST

[Modern REST](https://github.com/wemake-services/django-modern-rest) framework for [Django](https://github.com/django/django) with types and async support!
</div>

## Contents
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Official](#official)
- [Extensions](#extensions)
- [Tooling and Utilities](#tooling-and-utilities)
- [AI and Agent Tooling](#ai-and-agent-tooling)
  - [Official AI context](#official-ai-context)
  - [Official migration and generation skills](#official-migration-and-generation-skills)
- [Projects and Templates](#projects-and-templates)
- [Articles](#articles)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Official

- [Documentation](https://django-modern-rest.readthedocs.io/en/latest/) - Complete API reference and practical usage guides.
- [Source code](https://github.com/wemake-services/django-modern-rest/) - Source repository on GitHub.<!--lint enable double-link-->
- [Performance and Benchmarks](https://django-modern-rest.readthedocs.io/en/latest/pages/deep-dive/performance.html#performance-and-benchmarks) - Performance analysis and benchmark results.

## Extensions

- [diwire](https://docs.diwire.dev/howto/web/django-modern-rest.html) - Integration guide for the `diwire` type-driven dependency injection framework.
- [dmr-dishka](https://github.com/arturboyun/dmr-dishka) - Integration package for [Dishka](https://github.com/reagento/dishka/) with typing and async support.

## Tooling and Utilities

- [django-stubs](https://github.com/typeddjango/django-stubs) - Type stubs and a mypy plugin for Django projects using django-modern-rest.
- [django-mantle](https://noumenal.es/mantle/) - Typed model conversion for Django `QuerySet`s with official django-modern-rest [integration documentation](https://django-modern-rest.readthedocs.io/en/latest/pages/integrations.html#django-mantle).
- [django-health-check](https://github.com/codingjoe/django-health-check) - Simple health check endpoints for Django.

## AI and Agent Tooling

### Official AI context

- [LLMs support in docs](https://django-modern-rest.readthedocs.io/en/latest/pages/getting-started.html#llms-support) - Official guidance for AI-assisted development and upgrade workflows.
- [llms.txt](https://django-modern-rest.readthedocs.io/llms.txt) - Lightweight index for LLM context.
- [llms-full.txt](https://django-modern-rest.readthedocs.io/llms-full.txt) - Full documentation context for coding agents.
- [Context7](https://context7.com/wemake-services/django-modern-rest) - Up-to-date DMR docs for AI tools.
- [DeepWiki](https://deepwiki.com/wemake-services/django-modern-rest) - AI-friendly knowledge view of the framework.

### Official migration and generation skills

- [dmr](https://github.com/wemake-services/django-modern-rest/tree/master/.agents/skills/dmr) - Best-practices skill for building/maintaining DMR code.
- [dmr-from-drf](https://github.com/wemake-services/django-modern-rest/tree/master/.agents/skills/dmr-from-drf) - AI-guided migration from Django REST Framework to django-modern-rest.
- [dmr-from-django-ninja](https://github.com/wemake-services/django-modern-rest/tree/master/.agents/skills/dmr-from-django-ninja) - AI-guided migration from django-ninja / ninja-extra.
- [dmr-openapi-skeleton](https://github.com/wemake-services/django-modern-rest/tree/master/.agents/skills/dmr-openapi-skeleton) - Spec-first generation of DMR transport skeleton from OpenAPI 3.1+.


## Projects and Templates

- [wemake-django-templates](https://github.com/wemake-services/wemake-django-template/) - Production-ready project template with django-modern-rest and modern tooling.

- [spectacular-dmr-demo](https://github.com/gimntut/spectacular-dmr-demo) - Demo of gradual migration from DRF to django-modern-rest with a unified OpenAPI layer.

- [url-shortener-django-modern-rest-example](https://github.com/Peopl3s/url-shortener-django-modern-rest-example) - URL shortener API example built with Django and django-modern-rest.

## Articles

- [Why Django needs a new REST API](https://t.me/opensource_findings/938) - Short Russian-language overview of the framework's goals and core benefits.

- [Django Modern REST 0.1.0: First Public Release](https://t.me/opensource_findings/950) - Detailed Russian-language release post covering key features and ecosystem integrations.
