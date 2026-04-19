
to run: npm run start <URL>

using nvm: https://github.com/nvm-sh/nvm?tab=readme-ov-file#intro

uses npm:
 -creates package.json

in package.json:
    -devDependencies are used by the developer to run tests and other development tasks, not included in production 
    -dependencies are used in production, included when the package is installed as a dependency
    -start allows use to just run npm start to run the program

using jest testing runtime (maybe swap to vitest later): 
    -install using: npm install --save-dev jest 
        -is a dev dependency, meaning it is used by developer as test, so it has --save-dev
    -adds "devDependencies" to package.jason
    -installs node_modules folder (git ignored)
    -creates package-lock.json
    -in package.json, under "scripts", "test" is set to "jest"
    -needed to use babel for this project to get it to work properly
        -

using jsdom (an alternative is happy-dom):
    -install using: npm install jsdom
        -not a dev dependency, just a normal dependency so it's just used by the application not developer
