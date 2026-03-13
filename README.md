# Awesome Django Modern REST [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

<div align="center">
  <img src="https://raw.githubusercontent.com/kondratevdev/awesome-django-modern-rest/master/assets/logo-dark.svg#gh-light-mode-only" alt="Awesome Modern REST Logo - Light" width="100%" height="auto" />
  <img src="https://raw.githubusercontent.com/kondratevdev/awesome-django-modern-rest/master/assets/logo-light.svg#gh-dark-mode-only" alt="Awesome Modern REST Logo - Dark" width="100%" height="auto" />
</div>

<!--lint disable double-link-->
[![CI](https://github.com/kondratevdev/awesome-django-modern-rest/actions/workflows/ci.yml/badge.svg)](https://github.com/kondratevdev/awesome-django-modern-rest/actions/workflows/ci.yml)
[![Modern REST](https://img.shields.io/badge/Modern%20REST-0C4B33?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA4MCIgaGVpZ2h0PSIxMDgwIiB2aWV3Qm94PSIwIDAgMTA4MCAxMDgwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cGF0aCBkPSJNMiA3MDQuMDJMMTQ1LjQ1OSA0NjYuMTlMMjc3Ljg4MyA3MDQuMDJMMTQ1LjQ1OSA5NDEuODQ5TDIgNzA0LjAyWiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTE0NS40NTkgOTQxLjg0OUwyIDcwNC4wMkgyNzcuODgzTDE0NS40NTkgOTQxLjg0OVoiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik02NzguOTQ4IDcwNC4wMzVMMzQxLjIzIDEzOEwyMjcuMDcxIDMyOC4yNjRMNDM2LjM2MiA3MDQuMDM1TDMwMy4xNzcgOTQxLjg2NEg1MzYuMjVMNjc4Ljk0OCA3MDQuMDM1WiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTY3OC45MzcgNzA0LjAyNkg0MzYuMzVMMzAzLjE2NiA5NDEuODU2SDUzNi4yMzlMNjc4LjkzNyA3MDQuMDI2WiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTEwNzguMTcgNzA0LjAzNUw3NDAuNDUxIDEzOEw2MjYuMjkzIDMyOC4yNjRMODM1LjU4MyA3MDQuMDM1TDcwMi4zOTkgOTQxLjg2NEg5MzUuNDcyTDEwNzguMTcgNzA0LjAzNVoiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik0xMDc4LjE3IDcwNC4wMzVIODM1LjU4M0w3MDIuMzk5IDk0MS44NjRIOTM1LjQ3MkwxMDc4LjE3IDcwNC4wMzVaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K&color=35544A)](https://github.com/wemake-services/django-modern-rest)

> A curated list of resources related to Django Modern REST

[Modern REST](https://github.com/wemake-services/django-modern-rest) framework for [Django](https://github.com/django/django) with types and async support!

## Contents
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Official](#official)
- [Extensions](#extensions)
- [Typing and Tooling](#typing-and-tooling)
- [AI and Spec-First](#ai-and-spec-first)
- [Projects and Templates](#projects-and-templates)
- [Articles](#articles)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Official

- [Documentation](https://django-modern-rest.readthedocs.io/en/latest/) - Provides a complete API reference along with practical usage guides.
- [Source Code](https://github.com/wemake-services/django-modern-rest/) - Is available on GitHub.<!--lint enable double-link-->
- [Perfomance and Benchmarks](https://django-modern-rest.readthedocs.io/en/latest/pages/deep-dive/performance.html#performance-and-benchmarks) - Performance analysis and benchmark results.

## Extensions

- [dmr-dishka](https://github.com/arturboyun/dmr-dishka) - Provides integration of [Dishka](https://github.com/reagento/dishka/) dependency injection framework with types and async support.

## Typing and Tooling

- [django-stubs](https://github.com/typeddjango/django-stubs) - Provides type stubs and a mypy plugin for Django, making it easier to keep django-modern-rest projects fully typed.

## AI and Spec-First

- [dmr-llm-spec-first](https://github.com/milssky/dmr-llm-spec-first) - Codex skill that generates a Django project skeleton with django-modern-rest directly from an OpenAPI specification.

## Projects and Templates

- [wemake-django-templates](https://github.com/wemake-services/wemake-django-template/) - Can be used to jump-start your new project and already includes an example of using this framework with DI and all the modern goodies.

- [spectacular-dmr-demo](https://github.com/gimntut/spectacular-dmr-demo) - Demonstrates a gradual migration from DRF to django-modern-rest with drf-spectacular serving as a unified OpenAPI interface.

## Articles

- [Why Django needs a new REST API](https://t.me/opensource_findings/938) - A concise article (in Russian) on why Django needs a modern REST API and how django-modern-rest brings strict OpenAPI, full typing, async support, and high performance without abandoning the Django ecosystem.

- [Django Modern REST 0.1.0: First Public Release](https://t.me/opensource_findings/950) - A detailed release announcement (in Russian) covering the framework's core ideas, major features, and ecosystem integrations.
