# Awesome Django Modern REST [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

<div align="center">
  <img src="https://raw.githubusercontent.com/kondratevdev/awesome-django-modern-rest/master/assets/logo-dark.svg#gh-light-mode-only" alt="Awesome Modern REST Logo - Light" width="100%" height="auto" />
  <img src="https://raw.githubusercontent.com/kondratevdev/awesome-django-modern-rest/master/assets/logo-light.svg#gh-dark-mode-only" alt="Awesome Modern REST Logo - Dark" width="100%" height="auto" />
</div>

[![CI](https://github.com/kondratevdev/awesome-django-modern-rest/actions/workflows/ci.yml/badge.svg)](https://github.com/kondratevdev/awesome-django-modern-rest/actions/workflows/ci.yml)

> A curated list of resources related to Django Modern REST

<!--lint disable double-link-->
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

## Articles

- [Why Django needs a new REST API](https://t.me/opensource_findings/938) - A concise article (in Russian) on why Django needs a modern REST API and how django-modern-rest brings strict OpenAPI, full typing, async support, and high performance without abandoning the Django ecosystem.
