# Changelog

## 0.1.0-alpha.5 (2025-02-14)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/maisaai/python-sdk/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** OpenAPI spec update via Stainless API ([#18](https://github.com/maisaai/python-sdk/issues/18)) ([51c4025](https://github.com/maisaai/python-sdk/commit/51c40252cc130836f517ec20601618b67f5b5c43))
* **api:** OpenAPI spec update via Stainless API ([#21](https://github.com/maisaai/python-sdk/issues/21)) ([4b94f71](https://github.com/maisaai/python-sdk/commit/4b94f710dfcf6e0a3155ee1328d96dafe7b26efa))
* **client:** send `X-Stainless-Read-Timeout` header ([#60](https://github.com/maisaai/python-sdk/issues/60)) ([69e514f](https://github.com/maisaai/python-sdk/commit/69e514f736ef246a99c7b842521cf59a751a7814))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#64](https://github.com/maisaai/python-sdk/issues/64)) ([f7ad873](https://github.com/maisaai/python-sdk/commit/f7ad8737d8a8996062f6dc62e9ad8ecf34456dd5))
* **client:** compat with new httpx 0.28.0 release ([#31](https://github.com/maisaai/python-sdk/issues/31)) ([3494f25](https://github.com/maisaai/python-sdk/commit/3494f25077638c28d293cae09a251c6d6a75fd0e))
* **client:** only call .close() when needed ([#48](https://github.com/maisaai/python-sdk/issues/48)) ([2a8b3ea](https://github.com/maisaai/python-sdk/commit/2a8b3eae602602a012db86751b7569129fb1a02c))
* correctly handle deserialising `cls` fields ([#51](https://github.com/maisaai/python-sdk/issues/51)) ([8bab70c](https://github.com/maisaai/python-sdk/commit/8bab70c60cd7bf9e441173a0273ce17e0f41a302))
* **tests:** make test_get_platform less flaky ([#54](https://github.com/maisaai/python-sdk/issues/54)) ([0f53e2e](https://github.com/maisaai/python-sdk/commit/0f53e2eaf845b8631222747adbed6aef26e71aef))


### Chores

* add missing isclass check ([#46](https://github.com/maisaai/python-sdk/issues/46)) ([0e94ac2](https://github.com/maisaai/python-sdk/commit/0e94ac22ca8e33653888f357526433a23e82dad0))
* **internal:** add support for TypeAliasType ([#37](https://github.com/maisaai/python-sdk/issues/37)) ([c4f353f](https://github.com/maisaai/python-sdk/commit/c4f353f07fdb0a7f1a8b737f85973509c6aa6bb7))
* **internal:** avoid pytest-asyncio deprecation warning ([#55](https://github.com/maisaai/python-sdk/issues/55)) ([bc8b43e](https://github.com/maisaai/python-sdk/commit/bc8b43ef36216fbfac1526075402c1cd20d4af57))
* **internal:** bummp ruff dependency ([#59](https://github.com/maisaai/python-sdk/issues/59)) ([7882f2c](https://github.com/maisaai/python-sdk/commit/7882f2c5a49d968bafb60729ac31c831e2b8161f))
* **internal:** bump httpx dependency ([#47](https://github.com/maisaai/python-sdk/issues/47)) ([fb2bc94](https://github.com/maisaai/python-sdk/commit/fb2bc9496c5b7c66454d1b2e77c8bf8665a28ab5))
* **internal:** bump pydantic dependency ([#34](https://github.com/maisaai/python-sdk/issues/34)) ([1b764fd](https://github.com/maisaai/python-sdk/commit/1b764fdebbf53d067b1c208e9c9c124cab1ab76d))
* **internal:** bump pyright ([#32](https://github.com/maisaai/python-sdk/issues/32)) ([0ecc7ec](https://github.com/maisaai/python-sdk/commit/0ecc7ec95c31105611aa6abd11f230654e961009))
* **internal:** bump pyright ([#36](https://github.com/maisaai/python-sdk/issues/36)) ([a12e8fb](https://github.com/maisaai/python-sdk/commit/a12e8fbc0c7aa7e8e40280305ef08b382e091d34))
* **internal:** change default timeout to an int ([#58](https://github.com/maisaai/python-sdk/issues/58)) ([9b8fbb7](https://github.com/maisaai/python-sdk/commit/9b8fbb799000c30e15cdb7777e71aecf1584826c))
* **internal:** codegen related update ([#38](https://github.com/maisaai/python-sdk/issues/38)) ([07f9a2a](https://github.com/maisaai/python-sdk/commit/07f9a2a232504e9a4c5165e0fa8a1fc0a9cda823))
* **internal:** codegen related update ([#39](https://github.com/maisaai/python-sdk/issues/39)) ([0526011](https://github.com/maisaai/python-sdk/commit/05260113c3701215702d9b1024ccd5c0598afcad))
* **internal:** codegen related update ([#40](https://github.com/maisaai/python-sdk/issues/40)) ([6010846](https://github.com/maisaai/python-sdk/commit/601084637e5d988387413e25c0412f3b4de82c90))
* **internal:** codegen related update ([#41](https://github.com/maisaai/python-sdk/issues/41)) ([017e4c3](https://github.com/maisaai/python-sdk/commit/017e4c3a0a59b4e50beef1b6486642f9e9ccd7cb))
* **internal:** codegen related update ([#42](https://github.com/maisaai/python-sdk/issues/42)) ([738fb58](https://github.com/maisaai/python-sdk/commit/738fb58f48f2a7cdbdc1c5a04b8ac2e50eb4c3ab))
* **internal:** codegen related update ([#45](https://github.com/maisaai/python-sdk/issues/45)) ([a28dbb9](https://github.com/maisaai/python-sdk/commit/a28dbb952c8668b1fbd895979705646789522712))
* **internal:** codegen related update ([#50](https://github.com/maisaai/python-sdk/issues/50)) ([0f877e7](https://github.com/maisaai/python-sdk/commit/0f877e7b5d82c07647afaddb9f236181e286ad07))
* **internal:** codegen related update ([#52](https://github.com/maisaai/python-sdk/issues/52)) ([e097f1c](https://github.com/maisaai/python-sdk/commit/e097f1c81b5504db6d7761a845542a5dd300221f))
* **internal:** exclude mypy from running on tests ([#30](https://github.com/maisaai/python-sdk/issues/30)) ([3bcf1c9](https://github.com/maisaai/python-sdk/commit/3bcf1c92cd0d4614f3e433a875ff5c57deef884a))
* **internal:** fix compat model_dump method when warnings are passed ([#27](https://github.com/maisaai/python-sdk/issues/27)) ([d354f4a](https://github.com/maisaai/python-sdk/commit/d354f4a0dea8c17c8cb9d3651f726f92f8a7b81d))
* **internal:** fix some typos ([#44](https://github.com/maisaai/python-sdk/issues/44)) ([01228e6](https://github.com/maisaai/python-sdk/commit/01228e6aade70fd952ee192abdb2f90a4381fc92))
* **internal:** fix type traversing dictionary params ([#61](https://github.com/maisaai/python-sdk/issues/61)) ([d69c8ce](https://github.com/maisaai/python-sdk/commit/d69c8cecc1eb95971ad11814b5c39506b5a35ae3))
* **internal:** minor formatting changes ([#57](https://github.com/maisaai/python-sdk/issues/57)) ([218176b](https://github.com/maisaai/python-sdk/commit/218176bbb0aad125049959bf249298d9275276ef))
* **internal:** minor style changes ([#56](https://github.com/maisaai/python-sdk/issues/56)) ([0614b4a](https://github.com/maisaai/python-sdk/commit/0614b4a6d98d5f36c2abf99692cc249eec7b1462))
* **internal:** minor type handling changes ([#62](https://github.com/maisaai/python-sdk/issues/62)) ([3cde3a5](https://github.com/maisaai/python-sdk/commit/3cde3a52a5cc06e686bf44bebce5642d5ebbd6f0))
* **internal:** update client tests ([#63](https://github.com/maisaai/python-sdk/issues/63)) ([4596d45](https://github.com/maisaai/python-sdk/commit/4596d45e982f7d3fc3de025a1ba5574c590d875a))
* make the `Omit` type public ([#33](https://github.com/maisaai/python-sdk/issues/33)) ([72de306](https://github.com/maisaai/python-sdk/commit/72de3060418356f0b460f9b138a158e56eceb2a9))
* rebuild project due to codegen change ([#22](https://github.com/maisaai/python-sdk/issues/22)) ([29c8c9e](https://github.com/maisaai/python-sdk/commit/29c8c9e95ae569de0a785722d0773198b96912bc))
* rebuild project due to codegen change ([#23](https://github.com/maisaai/python-sdk/issues/23)) ([7c494c5](https://github.com/maisaai/python-sdk/commit/7c494c538e949dbccf6bcfa09a05c0119af5c4e8))
* rebuild project due to codegen change ([#24](https://github.com/maisaai/python-sdk/issues/24)) ([552ed44](https://github.com/maisaai/python-sdk/commit/552ed440c47d95c939942439344e3da2907b272e))
* rebuild project due to codegen change ([#25](https://github.com/maisaai/python-sdk/issues/25)) ([4c06923](https://github.com/maisaai/python-sdk/commit/4c06923e146784772fc5198485e0b46c336beb25))
* rebuild project due to codegen change ([#26](https://github.com/maisaai/python-sdk/issues/26)) ([2414a9e](https://github.com/maisaai/python-sdk/commit/2414a9e7d43f960247dc09534b429c7525838854))
* rebuild project due to oas spec rename ([#20](https://github.com/maisaai/python-sdk/issues/20)) ([9d1408b](https://github.com/maisaai/python-sdk/commit/9d1408bab9d6a93e0058ebe9a62b4f84d036f133))
* remove now unused `cached-property` dep ([#29](https://github.com/maisaai/python-sdk/issues/29)) ([5c8985c](https://github.com/maisaai/python-sdk/commit/5c8985c2e5fa6621d4801f4c3ccf44df58af0369))


### Documentation

* add info log level to readme ([#28](https://github.com/maisaai/python-sdk/issues/28)) ([ac21690](https://github.com/maisaai/python-sdk/commit/ac2169019646303ec6c9eff1da3e07c2b71a6115))
* fix typos ([#49](https://github.com/maisaai/python-sdk/issues/49)) ([baf1fbc](https://github.com/maisaai/python-sdk/commit/baf1fbc795d885fd3871cf3a65da1950b53e7391))
* **raw responses:** fix duplicate `the` ([#53](https://github.com/maisaai/python-sdk/issues/53)) ([ff88f4f](https://github.com/maisaai/python-sdk/commit/ff88f4fb37f793982750daffd89742f06edd9d0d))
* **readme:** example snippet for client context manager ([#43](https://github.com/maisaai/python-sdk/issues/43)) ([03b1d41](https://github.com/maisaai/python-sdk/commit/03b1d41f8bf0eb3b7e4374ed66655dc393530303))
* **readme:** fix http client proxies example ([#35](https://github.com/maisaai/python-sdk/issues/35)) ([90fa18a](https://github.com/maisaai/python-sdk/commit/90fa18a81017f3ee361bcdb1a1f5bc1164f20052))

## 0.1.0-alpha.4 (2024-03-05)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/maisaai/python-sdk/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* update via SDK Studio ([#16](https://github.com/maisaai/python-sdk/issues/16)) ([c67fc05](https://github.com/maisaai/python-sdk/commit/c67fc05ae116d31bb6113c12b26c4192d1d669ee))

## 0.1.0-alpha.3 (2024-02-20)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/clibrain/python-sdk/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* update via SDK Studio ([#14](https://github.com/clibrain/python-sdk/issues/14)) ([83399ce](https://github.com/clibrain/python-sdk/commit/83399cebe190801627a6e539c3c600a04a5b7151))

## 0.1.0-alpha.2 (2024-02-20)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/clibrain/python-sdk/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* update via SDK Studio ([#10](https://github.com/clibrain/python-sdk/issues/10)) ([fdaf14b](https://github.com/clibrain/python-sdk/commit/fdaf14b6a12e4f48258d1f69265674bc5f6c97ec))
* update via SDK Studio ([#12](https://github.com/clibrain/python-sdk/issues/12)) ([f7180ca](https://github.com/clibrain/python-sdk/commit/f7180caac484ef097a9a3fdd3c839556ac22e7a2))

## 0.1.0-alpha.1 (2024-02-20)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/clibrain/python-sdk/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* Add initial Stainless SDK ([7a26a08](https://github.com/clibrain/python-sdk/commit/7a26a0850b3fd6a61d0c594991c472342651f661))
* Add initial Stainless SDK ([e9c0cc3](https://github.com/clibrain/python-sdk/commit/e9c0cc39800c07a9dc15a1b43f6a70d5e9b2385a))
* Add initial Stainless SDK ([eb8af28](https://github.com/clibrain/python-sdk/commit/eb8af2844d4cd13010354caa949accc2566982f4))
* Add initial Stainless SDK ([ba243b2](https://github.com/clibrain/python-sdk/commit/ba243b21d5ae992aa9fbaef220340bf181b16a43))
* create default branch ([6c193d9](https://github.com/clibrain/python-sdk/commit/6c193d967adbc5b35b5eed3c630b2858c4720024))


### Chores

* go live ([#1](https://github.com/clibrain/python-sdk/issues/1)) ([733cb6a](https://github.com/clibrain/python-sdk/commit/733cb6a9e5cd962756db1b43ff385825dfa9f386))
* go live ([#5](https://github.com/clibrain/python-sdk/issues/5)) ([43658df](https://github.com/clibrain/python-sdk/commit/43658dff384a0c7732e1bacfc31ef135e899256c))
* go live ([#6](https://github.com/clibrain/python-sdk/issues/6)) ([1d6ffff](https://github.com/clibrain/python-sdk/commit/1d6ffffd039b68790ff0b54b7ce4ceb8b9ad049f))
* go live ([#9](https://github.com/clibrain/python-sdk/issues/9)) ([8baa20e](https://github.com/clibrain/python-sdk/commit/8baa20ebc8823b848466fca3ccdd2eb9eab3110a))
