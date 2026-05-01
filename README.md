


using nvm: https://github.com/nvm-sh/nvm?tab=readme-ov-file#intro

uses npm:
    - creates package.json

in package.json:
    - devDependencies are used by the developer to run tests and other development tasks, not included in production
    - dependencies are used in production, included when the package is installed as a dependency
    - start allows use to just run npm start to run the program

testing with Vitest:
    - install using: npm install -D vitest
    - adds vitest to devDependencies in package.json
    - in package.json, "scripts.test" is set to "vitest"
    - config can live in vitest.config.js for globals and environment options
    - run tests with: npm test
    - run once (no watch): npm test -- --run

using jsdom (an alternative is happy-dom):
    - install using: npm install jsdom
    - keep jsdom as a normal dependency because the application uses it at runtime
