# Web Development Examples

A polyglot collection of front-end and web-platform examples: markup, styling
languages and frameworks, scripting, component frameworks, and the data and API
formats that glue them together. Every example is a small, standalone,
idiomatic snippet rather than a project template.

## Layout

| Directory | Language / framework | Files | Validation |
|:---|:---|:---|:---|
| `html/` | HTML5 | semantic layout, forms, ARIA, tables, canvas, SVG, `<picture>`, `<dialog>` | `html5lib` |
| `css/` | CSS3 | reset, flexbox, grid, custom properties, animations, container queries | `sass` parser |
| `scss/` | Sass / SCSS | variables, nesting, mixins, functions, placeholders, loops, maps, `@use` modules | `sass` compiler |
| `tailwind/` | Tailwind CSS | config, `@apply` layers, responsive utility components | JS check |
| `webcomponents/` | Web Components | custom elements, shadow DOM, templates, adopted stylesheets | `node --check` |
| `javascript/` | JavaScript (ES2023) | DOM, fetch, promises, modules, closures, classes, observers, workers | `esbuild` |
| `typescript/` | TypeScript | generics, unions, utility/mapped/conditional types, decorators | `esbuild` |
| `react/` | React 19 | function components, hooks, context, reducers, error boundaries | `esbuild` |
| `vue/` | Vue 3 | Composition API, Options API, props/emit, `v-model` | reference |
| `json/` | JSON / JSONL | package + tsconfig, JSON Schema, JSON-LD, GeoJSON, JSON Patch, OpenAPI | `json` |
| `xml/` | XML | sitemap, RSS, Atom, SVG, XSLT, XSD, SOAP, configuration | `ElementTree` |
| `graphql/` | GraphQL SDL | schema, queries, mutations, subscriptions, fragments, federation | `graphql-js` |

## Tooling

```bash
sass scss/main.scss out.css                 # compile a stylesheet
npx esbuild javascript/modules_import.mjs   # parse/transform JavaScript/TypeScript
node --check webcomponents/custom_element.js
node -e "JSON.parse(require('fs').readFileSync('json/package.json'))"
wasmtime run ../algorithms/31_wasm/add.wasm # see also: WebAssembly examples
```

Related low-level and browser-runtime examples live in
`../algorithms/06_javascript/`, `../algorithms/07_typescript/` and
`../algorithms/31_wasm/`.
