# crawlect
2025.04.10 01:38

Generated with Crawlect.

## File structure

Directory tree.

- **crawlect/**  
    - [.gitignore](#f4aca847a0839bf0ecc4b539b518d189)  
    - [crawlect.py](#6bea7ebd390bd64ef0a32f9ffef5173a)  
    - [format.py](#b93cb4ee570a6381a51faf63b1b83e8b)  
    - [languages.json](#7bcc248ab64f1e00243d36895ca6820f)  
    - [output.py](#773017d6f93fc69b8fb7fd5a853427ef)  
    - [README.md](#7420f60d9af5d9ccf11e12c9e0be3620)  
    - [scan.py](#ff6c8e5c9d5f8eff49a0cac54a8b5bbd)  
    - `.git/`  
        - [COMMIT_EDITMSG](#9107a5dd03c321efd49065b1ab9f5777)  
        - [config](#9641181a2a5f75002a633baf2da8933d)  
        - [description](#04769364ac70f1aaacafa827483a0780)  
        - [FETCH_HEAD](#00f1ddadb991964dbd3683e21b1a7b24)  
        - [HEAD](#347410a6d4351444d8e4ce1085f2e5a6)  
        - [index](#8d9062d030923ed0d6b897ef6cc1800e)  
        - [ORIG_HEAD](#57a0f5bdb6c8cb9994eb3e10c32cdac9)  
        - [packed-refs](#c20eb2362cbb9ceea7285fbc5624f51b)  
        - `hooks/`  
            - [applypatch-msg.sample](#e584b0e9b2ddb234705796061e013dbc)  
            - [commit-msg.sample](#1e73d612a6a71209c2bec25b044b43c8)  
            - [fsmonitor-watchman.sample](#b78f8f81a44a832905785a499d222ef2)  
            - [post-update.sample](#75c972a8cf748bc76f8d670d7fd1ba0c)  
            - [pre-applypatch.sample](#e986d7be216d053efc460123c5862d81)  
            - [pre-commit.sample](#37f7154f543136e7be9e4f18547c0e4d)  
            - [pre-merge-commit.sample](#2405901a997579c4de572bda15712c97)  
            - [pre-push.sample](#f51d8b3754c7e0469774d6141b7c4bbb)  
            - [pre-rebase.sample](#06b670638221556429531ab7bfef1acb)  
            - [pre-receive.sample](#5ffe786b356ac7bad91cd9bdedc55e3a)  
            - [prepare-commit-msg.sample](#a6cb7191d6d2abd74e2285b5e7219c9e)  
            - [push-to-checkout.sample](#1ebd42b6d11e4ebbb612bd7e8252e3ac)  
            - [sendemail-validate.sample](#5b054391d189f7286f633c5c32346c3b)  
            - [update.sample](#a16e2645c2f4e048e04a68c1472738f2)  
        - `info/`  
            - [exclude](#f7cd24cab01ce1c90ecea877efbf2033)  
        - `logs/`  
            - [HEAD](#a460c44131cd70a63d6828b3f101677c)  
            - `refs/`  
                - `heads/`  
                    - [Alex](#1bec58a1cb9e0cebfa3edff274089d4a)  
                    - [dev](#b4a15fcf987862b8d395f9e60c4bd5bd)  
                    - [main](#15f39d11df6b164cf184a09cd994312a)  
                    - [yves](#10b77963c9cc28e3b2cd7c6a214aa3c9)  
                - `remotes/`  
                    - `origin/`  
                        - [Alex](#75f58a28af213cb00cff57d3a7fa7765)  
                        - [dev](#c2fe29082ab9c650f46f6521969367dc)  
                        - [HEAD](#d7b45c1e3677f637e55b9166aebbc1c0)  
                        - [main](#e6f13754638ab38af1cd5ee7be213ffc)  
                        - [yves](#ccc617adf0e82325c65390161fcddcbe)  
        - `objects/`  
            - `00/`  
                - [b0dcf83a4844de810da71c8a292551617fe536](#8218d21410702b6d9bc37c235dbe275a)  
            - `01/`  
                - [f64bc60f64bdafd3d3a836f6dec3f9c038b580](#57dbbe07dec2a7ba0f43bad84ae88a4d)  
            - `02/`  
                - [a633a03ede616f6989030094b20b1aacd450e4](#dcb3ed24caec2b9cffe9fae0bda02ab2)  
            - `03/`  
                - [b3b242ad99b8b0405d8b02290acecf028a73e8](#8daa92ce342a91f22f9ba4957591d51a)  
            - `05/`  
                - [5756a147423e71da1dc8e2639d4325f8cae3e6](#6bb3a99d2590c4f85577baf26ee897f2)  
                - [ba1f054f20d9e981742b725e8807f07ffcc759](#f135cf1bab74758b72c370175d61a484)  
            - `06/`  
                - [d14d95b72a09ba87a47d93aa96ec548f547940](#77cc0cd6c3d20261994206e15895658c)  
            - `07/`  
                - [7f1b9cd0e7d22605a67457cff7c29ac1809369](#b9fa88b9b8a20ce6e2ad58ba6b3bd71a)  
            - `0a/`  
                - [0d7a8d7bd8370a9539787ca3088f7ff48f7542](#a920a20230e271e4a89ae49f45f90dee)  
            - `0b/`  
                - [4af67ff6afcb09f7b044746698e3e8e086866b](#3a01282e8fed7986b6a8c3d67b050e71)  
                - [d7f4b90a3bc54d2a9101b1963332da629179ad](#e89e88ad50372c30ae2c5465b4de8647)  
            - `0f/`  
                - [9338f20d96a4dc07c029e4d1f4b59990754dc8](#e8213966177e27fa9504ab401a87d0e4)  
            - `10/`  
                - [2e09ef1ae0ac797f124d648d6ecbecd79550f3](#ea20ecddbb67fd3c6455a1711e6c9672)  
            - `11/`  
                - [2ea2ba6a337894f42e3fba2be392b1dd4639b1](#491d2a40ac905c18f178d6d535026f63)  
            - `12/`  
                - [2dfc6dcc39b668b18fa2513a3614e871f1f127](#d09b115fb8cfb39a907658cfb3c7d9cc)  
                - [7098054db882759b2db664d9183861e1a169fb](#b018d0dc5c4d0cd13584b0eadb31a50e)  
            - `16/`  
                - [242ffbf026fb2ea15abe83a7f82d835bebc26b](#1f5f8ed21ca2f5c9dbc3ab9b661a0c50)  
                - [5f7dc73136e2427c02c8b90180f397cf11526d](#6183d324301e1cc53dea3b84a64b7cbf)  
            - `17/`  
                - [34d08bd5fba993475d7167ce2a568220e0f101](#bd80e998700cfa12391a7a8b43a6c240)  
                - [72ba8aa5b453412d265cbafb5273308c5a6ee6](#18ff1a4929b24837316d94fd303eac7e)  
            - `18/`  
                - [21d28a35e090b94adafb87cd8f5dc69e66ed85](#5dfe84a69fd8bc499b782c01ce448730)  
                - [b90a9234fad117e72206a859869c46055a30be](#81010352fa3125a326e1412497e68818)  
            - `1a/`  
                - [e3777f70d209bc0c18c85343a78cfb5d21a78c](#68ba9611afa40ac910e92488e5bd45bc)  
            - `1b/`  
                - [dac8503c40763981f25e261a5dd4b8612efe89](#d98f2010d024bc3d14ad0c9a8fdca41f)  
                - [f5ca10119841734a11784af8e1ae13d7715665](#aed840153bc149f8ac7d2034e1c2bf42)  
            - `1d/`  
                - [ac2430996f9c34d64fdbc8197d01d74a534ae6](#def05886a8d4a5a7561cbd5888941751)  
            - `1e/`  
                - [96de1a7882c54608bd92e1e889f0a19a93dc57](#28a57add3072174d0b3b00e231152713)  
            - `1f/`  
                - [d620c516a43cb0473e8228b878bf583c66ffc2](#8f13c597a3ffbff8d6a44558ddb71fb1)  
            - `22/`  
                - [53183ef213685d2057396be8999e99f5cc0ddb](#d3c155f6a700a4cb320e817b32097e1e)  
            - `23/`  
                - [8d933c819aeed244ca45d8086edad8e6cf4259](#8ed3c7aaa1202b3b138e2a17cf9fc66a)  
                - [e61b89c12b0616de0f900bf46b326756e340ef](#72fab479727cd345ac24b36d204ec4b6)  
            - `26/`  
                - [26afd0b537a1ac28a84df80c630fcffdb6ae93](#ee9f956fac61ce7b3336b8478b816240)  
            - `2a/`  
                - [96c280bbfe6e52904bf77e7641663f25833d9e](#d8638894fc89f6699c9c97ac8b8fd2b4)  
            - `2b/`  
                - [779076870a060cb841429c788db4cdfd21285f](#11afd96500846c363d3d19b489d81eea)  
                - [9e091eac7d91c79141b44ef384ee2e95e1a80e](#94fda5cb2670dea24b2ecbbe3523be60)  
            - `2f/`  
                - [514e598b2f5dc8295ce650d7cf8136fad5fdf6](#b3f55af839dc202d8e03f206081d6bc7)  
            - `30/`  
                - [c6e635cd57737f1c50e0b67152d3f311b32ae4](#5be28ebfdea4b850985d34cf898cb08f)  
            - `31/`  
                - [2f3f1c4f7efc0f5353b22b49d3cd1b00371664](#b86bec3be163a1c95aad5169f4049c45)  
            - `32/`  
                - [6b55ab91595b964c2209ead7311ee17bedbd2a](#f0cd68619618579da686e39246b9dad2)  
            - `34/`  
                - [ccaccf4db0e20148db4deb7f1a6fea95ab0fc4](#b292f09dfe1f1587a3f12df2ed2287da)  
                - [e9ef6ed9e384948e8175480e2bf497662e386c](#6c5fb2b056fba40c7321864667abdd72)  
            - `35/`  
                - [55c74c11a39a2160ad857c8ce3adfc49325e81](#77d7b427d6f5bbd1eb22795e834eedb9)  
                - [96c5ba5a3ea44ca2016297d28ff84716c5b18a](#1ba26f2d84e946a3d5f1b77c756abb44)  
            - `36/`  
                - [6935740ecb3d605e1ab58d6cca02f550b9f2f9](#40b234d732b48625aa4c184fc31f047e)  
            - `37/`  
                - [ca437fc55c4a02e06c56b3503cfec2bb7b71b9](#d3b5059ec8d0cdf84bc075202169a0bc)  
            - `38/`  
                - [44acccf1411b2141f86f315a7e666c8d1c0e76](#6cbf9b8434e953d95e8b63b877dde4d9)  
            - `3a/`  
                - [d1cb0af4136c9683dc269c37297856bc65646a](#068c37bbb1812f2570d61405286a0d76)  
            - `3c/`  
                - [3c8ae4763ccada344fcc056266701eabaada06](#fb0ac7e21e285e6ba0ec72b2d0ac1e5d)  
                - [4ff8b5f93b2406d54867525ba260a6c6bb4566](#9a2979524899518e092a3c819636c5b4)  
            - `3d/`  
                - [3bd1f63ab6f6a922fe50b755dad05972042178](#6b946cc08792ee30d05b0fa86032563c)  
            - `40/`  
                - [afc81f5b2656ea29f400cb220d4dbafbb0a3b5](#bb9923e3ec42f317a1e72b05f0ccfb48)  
                - [ffdab00aa4e5ddc3bd764c1d1834eb0f1bb00b](#43c5c8a284c1e6155333870110d511f2)  
            - `41/`  
                - [52af2dcf3969684bbee631b5f3cc0bfff9dce1](#b375595a532565802f5b4ee320062681)  
            - `43/`  
                - [5558c7f3c8c199d7d7e5e151a45052a3e485c2](#c486765863a76bd02798d03fd1b71bdc)  
            - `45/`  
                - [60115ef9fbcd17fbfce20d0e8a0ffb85c89251](#ceeeace74eab5c66805900e741f85340)  
                - [8b87979e5736da9ef661bdedcdbc448390f8ac](#1847693ac6029c5a6c7c5c34cac8a490)  
                - [fc7071fa95bf73aff5692257a02b43b4f2ce19](#abfbb5c53931ce743ab1ae53308b9a9c)  
            - `47/`  
                - [fcc110941040e787b6948bcb1020376daca403](#5042a14f26fc2380fb11f407be188bb8)  
            - `48/`  
                - [5f1e3b21776b297aa520f330bfd533275cd211](#51f769560226ce9a7417822df76dad79)  
            - `4d/`  
                - [dfd835906cdeae7e31586f7c204fba4ee913b7](#f3e9868590e57c27d5f130eb71a38dfe)  
                - [f822354c726703e3e8db3b86c18413d5c5d77b](#b65dd7a9e596f5e0e4ed04959ec5839f)  
            - `4e/`  
                - [8c4b405aa6f8af409c8ffcae037cc1ea03c6dc](#8f3c515513b82875b525bbf8fa4f6c60)  
            - `4f/`  
                - [13ce6e1dd0562ff8305ccf0f0c90e950135aba](#16f9aa9c0d967937c0618f3411d9e7b9)  
                - [84b3f0694c04258f95bcb5c31ea7c55e034b44](#a0c2d202affbf1d49ba1a61befd289f5)  
            - `50/`  
                - [bac08c8f5b01f94fedc479203a81288e02336c](#1da6609ae5e99e92cd484b029c1cabd6)  
            - `51/`  
                - [099e4d2f6531e23203652594f103088781a43f](#18fd792e74ca0cb14a1e28f97c1d1523)  
            - `54/`  
                - [3816e1d5e8fbb31f0b034ebf9e0d147416df5c](#38d602ed1f0f9391c56d4ddd49e1a623)  
                - [61ca8ab3ac750384970e4670ce489397a16d40](#b3735d9c8f6bd64eb7a7100817798a43)  
            - `56/`  
                - [bc2d8efe39a154e95be8d0ae836ec6cfa7a0a8](#52601681cd9eafaa8e6ce61c7b923694)  
                - [f0068fa14dedd17351a71cc988f6ef660d897e](#449a8c1a67f4109a587277cfff37f300)  
            - `57/`  
                - [3351d56e9fe4fdaf521652d26cfbfc12ed9503](#ced287a226ca26f38f534721bdd57c89)  
            - `58/`  
                - [992d53a44d020ded1ee1652e425b9debd719e3](#b66c71c7df0601d7cd417628c0a9f9d9)  
            - `5c/`  
                - [2626cf1e7cf00df11854955914e006ff53afca](#5dcf37f93285afcffb8c93b25703c3c9)  
            - `5d/`  
                - [98b00c47d683c783beccbf7640975f84d52b95](#f62af8a3a649c0a2da5b87b360f11a07)  
            - `5f/`  
                - [49d2be65c0c45564685223cd67647c8f67a584](#2c1d3861ee55f0abcc51ef7445d07cb9)  
            - `61/`  
                - [4d702e549c3fab082ae71d5ddc532e65457b34](#0ec6451af825bdfeb86a083d15177570)  
            - `62/`  
                - [2d7d46ff35c3c13f5980932b1127a1b90325ba](#c38619236eca48fcffa85f12a43af42e)  
                - [a01c7ba57ac4cb67b6c490f37c030bd35aaa5f](#7fa43b060031da6dd80bd68de18a35d6)  
                - [a16c7606bf97ea2e3bb804c9e490b9d9e4154a](#0aa60b60fe1d7114cd68c52a7a0f91c4)  
            - `63/`  
                - [3183dffff898123fde19229ac9dff3a0d98863](#3df70fb4416fdd6673af68508b13a96f)  
                - [e689fcd2c4879d5bbcd2e50369f756b024527a](#3e200751ec4531407b34b16afed5f1b6)  
            - `65/`  
                - [26b34b6f5f8d9cdaf8739117a91f6e9e975bee](#c7f99d1ce3b248ce15db7bfa6c5ef7c9)  
            - `66/`  
                - [4b5776892ca726d26c8b98921215bafdc7ae69](#983731ef3199fcd964eaec9e6af3fe59)  
            - `67/`  
                - [9b1a992ba8ac4ec3a373e460dce752882d4182](#283ad5392a53827a28e256ea162def9f)  
                - [ecfd52e6a410bf67282be8cd47d69eb65b8258](#c2c904d631e4b2a3237c10323936fa8b)  
            - `69/`  
                - [5ef5d6f082871652d1a143304332475eb1d509](#83f9cf15249a8e7af91c9e7b5c0ee52e)  
            - `6a/`  
                - [fdc88309a2f0135766f1cf5b0aba5fc5aaa1bc](#f03675ca6a65dabb02acc8cfbfe96c71)  
            - `6c/`  
                - [2ceafa55f871cb28e430d4a0785a1e6915d292](#4ebc4789222184fca4dec659f24f0c56)  
                - [f76b264050bb7bcd073ef74fa2e7f824cde560](#b6ec81e64d608bec2c8096efeadc0b34)  
                - [f7883038499eb4748cb65946b03bfa910551b9](#f72a905683a9b6b3b68ba90499442efd)  
            - `6f/`  
                - [10fecbc1c52017568cb0c5f9fa937ec98b6e8f](#99cdab36b18e28c05514b85c9443bda2)  
                - [4fae3513ed50a712833b4be45438d303ab3927](#f5c82a7f9f3f80180cbc8e378fd70940)  
                - [bfc2ecc99ea6163d6900731974424f8fbd1e5c](#c64025c0a42e89f89c2b635f1b8cee34)  
            - `70/`  
                - [283585533513da306a5ad54ddefe83e58f7213](#81c7c4f62c03b352a3a156d3b006bb9d)  
            - `75/`  
                - [48a4928e2a6f1ff24f3de4acb866a8e8cdaf40](#4fbf1b48082a79a07faf931436c7923c)  
            - `77/`  
                - [3de3c0fb393eac437a043156d29d1f3ba97a2b](#648aa9ad74fda2ba978b22069edaca19)  
                - [bb915c1bf5535fa34efdf65d7e2b5b5da26547](#084b833c94fb467162e1f6217164c742)  
            - `78/`  
                - [2ae81f095e323eaafa547d5698c65eb490d606](#769df9fd4609942ed1b7907958276347)  
            - `79/`  
                - [c8548d9d1fb5d12097fa57e3f710276bb03258](#91767f8ddcc6100580b40e3093a525c1)  
            - `7a/`  
                - [0d59b39d4f4984f242c1d0a3bae48be451dddb](#34591e3af6ac9f6f64f912f1533fd344)  
            - `7b/`  
                - [0e6009851021ceb9845a9735523aa68ccdb9dc](#4a27f9a76dc357de043c855851d67cc6)  
            - `7d/`  
                - [5af85164eaed5642a651dbf4584e0d0186e4e7](#861f3c82361bca4308cf0faf33b6a6ac)  
                - [c78684a2a061d1521f898e1f0dbc4e6777e7e1](#34d9c17e7009da2e4f3dcd467e5dc489)  
            - `7f/`  
                - [4ea9ce1159d253c66a779428b9a7993b20b611](#d7cbd78dfe0a56f7407a2fa97ae2bfb7)  
            - `80/`  
                - [d6c07c321fa31b0510cc757a62afe8c885ad08](#fe99625cc7cff76328952b21d992376b)  
            - `81/`  
                - [c765c26fdb5e78671b2e890f9c4958b54a5ae1](#912c89134b201d301b86c99dda80942c)  
            - `88/`  
                - [ba69bd95c3d67f31875b519dcb5c6cd2766aed](#f75c0f3b6f142bae5c1cb8108b0fe881)  
            - `8b/`  
                - [59eaafed90e14156b6a91a19f4800f5615a7a1](#7da583a4695107f7fe6c458ffbef96af)  
            - `8c/`  
                - [c16e05826a754545548b06539c3d51408ac257](#28048594f79ba6eb9ba5e884fd206e38)  
            - `8d/`  
                - [094c6a385091baf6dfe749641815bdc1e6ee8f](#1aea4d397b08378f131fdbb09f6d57d0)  
            - `8e/`  
                - [b819d0b4cbad6716b1e4fe3b6a4148a4786bc3](#2c5a0603546f8db4c157eb820a0c7121)  
            - `90/`  
                - [62950116f3f8eede31d1e179ea55b3fc8094a1](#4d502f87752aaf9b5963f176b16ce2e8)  
            - `92/`  
                - [f6e07c6b4c9ce8147f4411ed2242ca8ba87888](#c2aba26e81ee0e16c54d9b7e099e7b6d)  
            - `93/`  
                - [4e6ea43e33aa6ba9d15aed58628c2d3e3ef471](#7db30d00299c8c00fff8f7148b691517)  
                - [4eb54c557f65beedc649472c60a09772549c25](#25669daaa5f227f15c7aa2e438eb5999)  
                - [bf9985d73e77092681346e9d52166acd38f237](#700933ea84992547f4ae520ec0938a90)  
            - `94/`  
                - [38c19ee8e241e073821345a1a2bfe9c08e0096](#5c6359829f2cd4ea13807c96128908ac)  
            - `95/`  
                - [424ea67996a0ed9c249b7cf4a5e025370ac7fd](#aa01cc6e916498d38adc120606039416)  
            - `97/`  
                - [5a1ade779f0427af052d4a4b09c609598a18c3](#6948b47a14a281787d36e5fd118b7f8b)  
            - `98/`  
                - [c1f39b3f60b995e38bae647e397311a55c02a8](#c74410749548dad223a37ce69dd8c86d)  
            - `99/`  
                - [558d3f74ff673beb2512a10747e059e824d998](#d0cf6b5ad4d8be915a143391b1594253)  
            - `9d/`  
                - [dcb73c3a470f16297b6cd5c9c117cbd23b3b0a](#a29f39baaeeb24a366c0d0f13fab0697)  
            - `9f/`  
                - [6313967240101d454d27c0c048b4f87cff6bda](#7892d62ad9d8f94b3dcae2c24d7036fa)  
            - `a0/`  
                - [697025b3e8080b97095cfa0d25b7d2734231c9](#aa34c596229865da24730986482f2ce4)  
            - `a1/`  
                - [45057f5b8c8286b4d37abd483dbda8667b021f](#d2c25d00e81bac8717256d94eaa5088e)  
            - `a2/`  
                - [d102b7a29f2e546876af4753f787d35bfab599](#9636002c40cc25d97eac5ea2c79d6083)  
            - `a3/`  
                - [4e52c169214a785655bae76a93601f6ebf0147](#7994591eec30cd6774183a94e12f6a18)  
                - [c98f437a106c80a61242936afc9946fa415197](#42c91368b136c1aa12c3e44619ca7f60)  
            - `a6/`  
                - [aa870773b09b06aa6140c13b46bca73e1a58bd](#5c951a9e211309b22ceec256753495a8)  
            - `a7/`  
                - [9c41c6a7010b03cf9734dbb2ac3281b7d655a1](#36fafa79ddb41afd5f0dbaed55162aeb)  
            - `ab/`  
                - [e5987efc5a9bf32a3ff9fb081fe9793244cead](#2fda0a4c27863539e85f021035d7ca39)  
            - `ac/`  
                - [1b929027f394d65146efc2d244d3baa36c7542](#e7de16f5bebd013e3a95e67b51b5e781)  
                - [b77f3a1fda5c1d03fa7a868b28f11a594ec606](#3dcdec48c7fad36979b500e09f6c55a7)  
            - `ad/`  
                - [444b8444407d1278e730ff660275d7f364d0d4](#b2a9c66abbfbcb89473042689cb7b4c3)  
            - `ae/`  
                - [3a75a30304b6c28b424b0b4c4c677cb61b07ef](#fba943d17c5a7b0a6612e53c3257f90a)  
            - `af/`  
                - [e1f150947d7914ac5a3ec4ce460776fb77a496](#ee50ec8d47e06bea19b9cbb8f6c15f10)  
            - `b0/`  
                - [b70653b1ce1a036afc80a2665317bb1bcce941](#b561c396bd50fb6b2dc69b81535b42b8)  
            - `b3/`  
                - [5f683b265fdf1efabaca0923c1d86edbf7a351](#37d0dd7d775937d5da9777916cdad65b)  
            - `b5/`  
                - [eeb59d4285b0e26c93bd5c2439e5e67b36d2c4](#8546cbd5765cd4b7e1d304d5edef78ae)  
            - `b6/`  
                - [4109a585ef36b3384baed778db8951d6fc0b7d](#b40ea7537cbf71249c989f7642708fdc)  
            - `b7/`  
                - [35469715240efcf3c67c50d8689491891b59b4](#fb5f04e246175735bdba18f01c127d3d)  
            - `b9/`  
                - [9f50148a1a0bdce9f7f93b157251de1e8167dd](#e56fbbd332577d879031fe56640fcb98)  
            - `ba/`  
                - [17e0d5664a322ee0031c049a2b2e24bded20ba](#dd2dba2842bc881ebf279782893bbe6f)  
            - `bb/`  
                - [77a7e55d70b0b79953c5835f40d66d84c98c3e](#fe93709ed6be4a2d55629684a1e5e71b)  
                - [e187722acf2db9b87ea3a770cdc064026d29e7](#b59cab1a363d27c6fa464307df8839b4)  
            - `bf/`  
                - [d6ec3fbc8f3d4865368a18b4a0b7bf15e279ea](#60cae2cf8c94ff4c64a8900b10436753)  
            - `c0/`  
                - [a2cd506b7390f8f1d144b7bcbe038263dc72fa](#e3b40806bd93a79913a222033c92bce1)  
            - `c1/`  
                - [cf41e90d3e6369e8428439996353e76956b963](#7e05e1d6e93bbea366a921471d0d182b)  
            - `c3/`  
                - [35db23d59680c165335eb3afbca2aa8c9e8bd4](#4b3b1782041b0e3b6e656f72cedf3bc6)  
                - [380b1bc547017efef34f480646418e35b683bb](#bc01f17aa765902fcb3afa5a9a20fbfe)  
                - [cf7195e19d653ed9ab3e862fe1fa1bf3280888](#542ca9d8a31115c67ed52609f2cf5a84)  
            - `c6/`  
                - [925797174f82f1a628cd440b449d28c5b25f3a](#b446383e19d333b0f242cb5d8d47d532)  
            - `c7/`  
                - [df06b807a080bdd7a6c042e81f202d5196beb3](#abefefc64db3b9abfeb3cc4d0c6d6c03)  
            - `c9/`  
                - [1e7865c38ed3e0d26b960b9f8ee11e8dc0c6fd](#ddaf7fcc5c287bee7e8e236d6b62adf5)  
                - [fc8139c28cf7d137ce12e86a5ff8a1464c88c5](#72814b86ed6e1d3fdc77b0b50c97770c)  
            - `ca/`  
                - [77be5f899fc8f6525b1412851016cb24d86fc6](#0089a57409bf997c72b612458fc77ecd)  
            - `ce/`  
                - [1e1301f1de81b98f467cc40c97d0c7e06b3088](#01b45395092ffe2b028909b5f0705f2a)  
            - `cf/`  
                - [dcb818e67edb6b6c47f916ea8b90e799dd0957](#3143a7f1eb6ac2609b211d84f75a2e26)  
            - `d0/`  
                - [afd9760f867928b546c76be5c5e5393e84205d](#8e6a0990a7a252d9bf42db95efa5fb02)  
            - `d1/`  
                - [087e1fd637ddd2a385cce23f469116af9d019e](#205abf38f8f657f4d2c3694787fc26e0)  
                - [57082d09d153fb16d5e1fd58b9dd68d2ac3723](#139f2cbd6ac74aed60b2d7aacf5fec31)  
            - `d3/`  
                - [c88dc04875e69dd2c531ebbb05a97ee46b8ed7](#2abcd431510d28c9ab6df3fa915a4857)  
            - `d5/`  
                - [307312c5b7385c0e4c6dbc653b044a04ff97ac](#07fd5b9f6ccfbae2b84e7b6fc33d0e29)  
            - `d7/`  
                - [33a248a8b952cb37dc71f30082437d5c8c423f](#f45adb21d4915209422b798cc452b7d5)  
            - `dc/`  
                - [199a2595ccf030883cdebd225ca6b70d776d3e](#5a91c9bce2c3fc4d0b777f967d8a7187)  
                - [b77f9bec75373db0049bbb9521bc7a806ef8ea](#afe7b690233d7a35d097ed64ed2853d5)  
            - `df/`  
                - [191f653201924ffeebfe77e4775c229b4c247a](#612865fa2ca9ad0ad567f49d56fd5347)  
            - `e0/`  
                - [1d84ea54104f2d60f8acbf3b3afa3a75f02a2e](#159caac958f4bd2ef12e1a8329608b08)  
                - [213cf7bae592e3202438282d5357c0272eeb53](#9dbdc5b981048ec5db201516bb8c83e1)  
                - [8f9d82201b8076a2305971cebdfeb45883df6a](#3147fba0dc1bba1b88900a990f9a2a34)  
            - `e2/`  
                - [4a375e9c669ce86470ff9b09d2ea1a86d02cd1](#3ee95b38815ef3da77a7c956027540bc)  
                - [c3376b1b891f6d39f0ee0fa1d90db0254b1e87](#373bd9871037a430c9ca6bdd3bd79cc8)  
                - [f0de0c07269b16e8350d76f81de9fc105e03b0](#1bc53ac215d07522d742fbf09ccc6b7c)  
            - `e3/`  
                - [493c30074cfaf2adfa9cc4cc7484e9acc14fbd](#950c6494daa5f1273e77241b09a8bfb2)  
                - [4ca624ec54a9a1446ac68b632f5183a34d1893](#d2b3b48d90107a4c18c4eca3b862a736)  
                - [d7f30d6cdd51c8d44d9c6b49c1733bd4bc20e2](#c403520c03ddb44238d3a2c270258e9e)  
            - `e4/`  
                - [bd78055125fda48837faa6c51755e0ac3a0f74](#49abef3d136a2654a114b9a88047d741)  
                - [ea3c96f31e0c21e90f873c340059ff253e0d7a](#80c6183fd1984277078462e2d338c405)  
            - `e5/`  
                - [0c00adfdcdc7f7eac179a2fb419e3e18cb650c](#d34b5d8a53fad0891d7b7814eaed86dd)  
            - `e8/`  
                - [2a6a80e57ba3967da598e091b9b72c15624c5b](#19bc57010c819e6f76168182b8a21f4c)  
            - `e9/`  
                - [13fcc65d5d5385e3d9b55d7a0f2c03909a8b74](#3e18b44fc264219a8f6c71660b48aeeb)  
            - `ea/`  
                - [96809835a37b3be4e445c028942f698d589bb8](#1e2051de160d5d7f7c0f45cabdfaa15a)  
                - [99900d2349112bb676a734c36438ca827c8ed1](#bd40d422d35b1693522e4c5c42504f86)  
            - `ec/`  
                - [9b58df6f0ead4600d44138359b3ca0398e40a3](#43e77320df984c1d331ce232ad3b5fae)  
                - [a4d4ac3e39e094752fa2414bde015d2f1f9cd9](#1037bccea3fa7ca032b5d5aed4caa468)  
            - `ed/`  
                - [47e7bdb6da882114614cbb69fba6a439e31360](#ff862bd52f5bb05c9ccfa3e51ff6dcc4)  
                - [aa3833096e84c3e3b74e3480144ff27cd5996d](#79eac9883e2a2167f6040b01dd2dfff3)  
                - [aec62c666b3d7e74a9a5b69d5b8736b1d6a037](#2dcc81f8131eb7ddecf0a28d61d38b6b)  
            - `ee/`  
                - [880b9f61b6d52259e2d63b2d48b2c130c07c08](#5c1c790a6e1a92754ac07103bd442012)  
            - `f0/`  
                - [9864aa230455aaa8fc1dc69c72d8630c2a71e9](#01afbaa420a7991a9a4efaadc602b268)  
            - `f2/`  
                - [4aab9a025019b126e4afade745972976c7b396](#f3002b316164404e2d400a0a7fccf408)  
                - [975d673ef63c9e7053a780069e6ca24d0e4546](#fb538401e01e50d9128ab5c21bc6ffae)  
            - `f3/`  
                - [72d5080b65692aedb80d48f19585810874a21e](#8c7287bb30c890b8d04e37ca770c13dc)  
            - `f4/`  
                - [5dbe53c3b682b22a72b4f446d10252b939fafe](#d1707e29446f08ae9afc6f3a9adfc86c)  
            - `f6/`  
                - [2cb47853ffc8b1de49ad39fa499ad6b530753b](#eff7949e1bb62e44a0e6722c09ef98cd)  
            - `f9/`  
                - [211cc1fd0c107aceedbb23bb4a0ac20760e136](#87ccffcc0b43ab71f72436c89a96bcd4)  
            - `fa/`  
                - [712c05040518da5b0b18708933fd70a148069e](#5318c2f3931d1c8cd5ec9237499650c6)  
            - `fd/`  
                - [a7087dcb6450ebd0b80cbc0b88cf0ffef07a16](#0461deb16fe831bfb5e6161de3ee4233)  
                - [eb60232737294bb9a1b2b96ff83f118dfdf098](#a44e3a7e86c2fdc0b2617f7cbdbb0ccf)  
            - `ff/`  
                - [83edd8c69782adb6c53185c99dc68e5e52ba00](#1c405f89916f238445bc5d79bdfc9b96)  
                - [911184668e4a061c737ac1498f1aefa7abbfd1](#cae018acc7dbffcc5a51089abcd00a1e)  
            - `info/`  
            - `pack/`  
                - [pack-94a8b021557f768c1ce959793e0afc8f957cab44.idx](#4807efe66a6b0a4cf4d8044a53ff702e)  
                - [pack-94a8b021557f768c1ce959793e0afc8f957cab44.pack](#043d92a48fc1d5173f99d782c2b8dea4)  
                - [pack-94a8b021557f768c1ce959793e0afc8f957cab44.rev](#ee18ae90ea455cfc529c503321ea5736)  
        - `refs/`  
            - `heads/`  
                - [Alex](#05e40a3198f115f800c786250c9c8b30)  
                - [dev](#ce96c1f6753032fa4b3140abdb30a8ae)  
                - [main](#0df99a058a0668e456aa018bd0575e76)  
                - [yves](#e6806bdfe55681c4f0850c9d97b9ea79)  
            - `remotes/`  
                - `origin/`  
                    - [Alex](#6843477a225e01dbe11bd0a7eeeac0fe)  
                    - [dev](#4929df26a52d10130057276b827ab1a5)  
                    - [HEAD](#7022ac1751805943e4a77f9efa5032e9)  
                    - [main](#27c845a973abe1b1682e5b9b2a157183)  
                    - [yves](#e506884d3cdc40c1d98fdfeb2db0b4a2)  
            - `tags/`  
    - `.idea/`  
        - [.gitignore](#1bd718d1d601e0cf83b445d1c902e1a4)  
        - [crawlect.iml](#072dd9adf55c124b838b19b0445b17ea)  
        - [misc.xml](#3e6fa50ac5b862a61c578be7a1137ea2)  
        - [modules.xml](#77620dde52ce244914a8459f52dcffb4)  
        - [vcs.xml](#fdd4e0cf92465a832b219796ad4073e1)  
        - `inspectionProfiles/`  
            - [profiles_settings.xml](#99eb69626b3ce864a04eb3cbb6eb152b)  
    - `__pycache__/`  
        - [crawlect.cpython-313.pyc](#f52b6b91f478752b08945673de151a98)  
        - [format.cpython-313.pyc](#3a4f596da884b56fbafbb554e9d9b696)  
        - [output.cpython-313.pyc](#d109dc8ad4f663007dc1349e90b2c0bd)  
        - [scan.cpython-313.pyc](#82703e032379976d54670e783c33ec65)  


## Files:

<h3 id="f4aca847a0839bf0ecc4b539b518d189">.gitignore</h3>  
`.gitignore`

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

```
<h3 id="7420f60d9af5d9ccf11e12c9e0be3620">README.md</h3>  
`README.md`

````````````markdown
# Crawlect – Crawl, Collect & Document Your Codebase in Markdown

**Crawlect** is a Python module designed to *crawl* a given directory, *collect* relevant files and contents, and *document* the entire structure in a clean, readable Markdown file.

Whether you're analyzing someone else's code or sharing your own, Crawlect makes it effortless to generate a comprehensive project snapshot — complete with syntax-highlighted code blocks, a tree-like structure overview, and fine-tuned filtering rules.

## Why Crawlect?

When starting with a new project — whether you're reviewing, refactoring, or collaborating — understanding its structure and key files is essential. Crawlect does the heavy lifting by:

- Traversing your project directory (recursively if needed),
- Filtering files and directories with powerful inclusion/exclusion rules,
- Masking sensitive data (like `.env` values),
- Embedding file contents in Markdown-formatted code blocks,
- Automatically generating a well-organized, shareable `.md` file.

## Use cases

- Quickly understand an unfamiliar codebase
- Auto-document your projects
- Share code context with collaborators (or *LLM*!)
- Safely include `.env` files without leaking sensitive values

***Think of Crawlect as your markdown-minion — obedient, efficient, and allergic to messy folders.***

## Crawlect – User Guide
**Crawlect**, the tool that turns your project folder into a beautifully structured Markdown digest — effortlessly.

## Installation
Crawlect currently runs as a standalone module. To use it, simply clone the repo or copy the files:

```bash
git clone https://github.com/yvesguillo/crawlect.git
cd crawlect
python3 crawlect.py
```
*(Packaging for pip? Let us know. We'll help you make it pip-installable!)*

## Quick Start
Generate a Markdown description of the current directory:

```bash
python3 crawlect.py -p . -o ./description.md
```
This will scan the current folder recursively and write a structured `description.md` including the contents of most files.

## Usage Overview
You can run Crawlect via the CLI with plenty of flexible options:

```bash
python3 crawlect.py --path ./my-project --output ./my-doc.md
```
Or dynamically generate unique filenames:

```bash
python3 crawlect.py --path ./my-project --output_prefix ./docs/crawl --output_suffix .md
```
You can filter files and folders:

```bash
# Exclude .png and .jpg files from listing
--excl_ext_li .png .jpg

# Include only .py and .md files for writing
--incl_ext_wr .py .md
```
You can also:

- Limit depth (`--depth 2`)
- Disable recursive crawling (`--recur no`)
- Enable the directory tree overview (`--tree yes`)
- Sanitize .env files (`--xenv yes`)

### Example Command
```bash
python3 crawlect.py \
  --path ./awesome-project \
  --output_prefix ./docs/snapshot \
  --output_suffix .md \
  --excl_ext_li .log .png .jpg \
  --incl_ext_wr .py .json \
  --tree yes \
  --xenv yes
Creates a structured markdown file (with a unique name), ignoring noisy files and including `.py` and `.md` contents.
```
### Tips

- `.env` files are *auto-sanitized* — values are replaced by `YourValueFor_<varname>`
- Inclusion rules overrule exclusion
- File name rules take precedence over extension rules

### Module Mode

You can use Crawlect as a **Python module** too:

```python
from crawlect import Crawlect

myCrawler = Crawlect(path=".", output="./project_overview.md")
myCrawler.outputService.compose()
```

## Planned Features (ideas welcome!)
- *Git* related filtering.
- *HTML* output
- *LLM* API integration.
- Optional syntax highlighting themes
- GUI launcher (who knows?)

## Architecture:

```text
                           +-----------------+
                           | User CLI        |
                           +--------+--------+
                                    |
                                    v
                           +-----------------+
                           | Crawlect        |  <== Main class
                           +--------+--------+
                                    |
          +-------------------------+-------------------------+
          |                         |                         |
          v                         v                         v
  +----------------+       +--------------- -+       +-----------------+
  |  Scan          |       | Format          |       | Output          |
  |  (List files)  |       | (Detect type &  |       | (Compose final  |
  |                |       | insert codebox) |       |  Markdown file) |
  +-------+--------+       +--------+------- +       +--------+--------+
          |                         |                         |
          v                         v                         v
    Files to list            Codebox strings         Markdown composition
       (Path)                      (MD)                     (MD)
```

- **Scan**: Crawls the directories based on inclusion/exclusion rules
- **Format**: Detects file type & builds Markdown-friendly code blocks
- **Output**: Writes everything to a nicely structured `.md` file

***"Documentation is like a love letter you write to your future self."***  
*— Damian Conway, we believe. Or some other wise code-wizard.*

## References and thanks
### Markdown code syntax table - From [jincheng9 on GitHub](https://github.com/jincheng9/markdown_supported_languages)
| language | ext1 | ext2 | ext3 | ext4 | ext5 | ext6 | ext7 | ext8 | ext9 |
|---|---|---|---|---|---|---|---|---|---|
| cucumber | .feature |  |  |  |  |  |  |  |  |
| abap | .abap |  |  |  |  |  |  |  |  |
| ada | .adb | .ads | .ada |  |  |  |  |  |  |
| ahk | .ahk | .ahkl |  |  |  |  |  |  |  |
| apacheconf | .htaccess | apache.conf | apache2.conf |  |  |  |  |  |  |
| applescript | .applescript |  |  |  |  |  |  |  |  |
| as | .as |  |  |  |  |  |  |  |  |
| as3 | .as |  |  |  |  |  |  |  |  |
| asy | .asy |  |  |  |  |  |  |  |  |
| bash | .sh | .ksh | .bash | .ebuild | .eclass |  |  |  |  |
| bat | .bat | .cmd |  |  |  |  |  |  |  |
| befunge | .befunge |  |  |  |  |  |  |  |  |
| blitzmax | .bmx |  |  |  |  |  |  |  |  |
| boo | .boo |  |  |  |  |  |  |  |  |
| brainfuck | .bf | .b |  |  |  |  |  |  |  |
| c | .c | .h |  |  |  |  |  |  |  |
| cfm | .cfm | .cfml | .cfc |  |  |  |  |  |  |
| cheetah | .tmpl | .spt |  |  |  |  |  |  |  |
| cl | .cl | .lisp | .el |  |  |  |  |  |  |
| clojure | .clj | .cljs |  |  |  |  |  |  |  |
| cmake | .cmake | CMakeLists.txt |  |  |  |  |  |  |  |
| coffeescript | .coffee |  |  |  |  |  |  |  |  |
| console | .sh-session |  |  |  |  |  |  |  |  |
| control | control |  |  |  |  |  |  |  |  |
| cpp | .cpp | .hpp | .c++ | .h++ | .cc | .hh | .cxx | .hxx | .pde |
| csharp | .cs |  |  |  |  |  |  |  |  |
| css | .css |  |  |  |  |  |  |  |  |
| cython | .pyx | .pxd | .pxi |  |  |  |  |  |  |
| d | .d | .di |  |  |  |  |  |  |  |
| delphi | .pas |  |  |  |  |  |  |  |  |
| diff | .diff | .patch |  |  |  |  |  |  |  |
| dpatch | .dpatch | .darcspatch |  |  |  |  |  |  |  |
| duel | .duel | .jbst |  |  |  |  |  |  |  |
| dylan | .dylan | .dyl |  |  |  |  |  |  |  |
| erb | .erb |  |  |  |  |  |  |  |  |
| erl | .erl-sh |  |  |  |  |  |  |  |  |
| erlang | .erl | .hrl |  |  |  |  |  |  |  |
| evoque | .evoque |  |  |  |  |  |  |  |  |
| factor | .factor |  |  |  |  |  |  |  |  |
| felix | .flx | .flxh |  |  |  |  |  |  |  |
| fortran | .f | .f90 |  |  |  |  |  |  |  |
| gas | .s | .S |  |  |  |  |  |  |  |
| genshi | .kid |  |  |  |  |  |  |  |  |
| gitignore | .gitignore |  |  |  |  |  |  |  |  |
| glsl | .vert | .frag | .geo |  |  |  |  |  |  |
| gnuplot | .plot | .plt |  |  |  |  |  |  |  |
| go | .go |  |  |  |  |  |  |  |  |
| groff | .(1234567) | .man |  |  |  |  |  |  |  |
| haml | .haml |  |  |  |  |  |  |  |  |
| haskell | .hs |  |  |  |  |  |  |  |  |
| html | .html | .htm | .xhtml | .xslt |  |  |  |  |  |
| hx | .hx |  |  |  |  |  |  |  |  |
| hybris | .hy | .hyb |  |  |  |  |  |  |  |
| ini | .ini | .cfg |  |  |  |  |  |  |  |
| io | .io |  |  |  |  |  |  |  |  |
| ioke | .ik |  |  |  |  |  |  |  |  |
| irc | .weechatlog |  |  |  |  |  |  |  |  |
| jade | .jade |  |  |  |  |  |  |  |  |
| java | .java |  |  |  |  |  |  |  |  |
| js | .js |  |  |  |  |  |  |  |  |
| jsp | .jsp |  |  |  |  |  |  |  |  |
| lhs | .lhs |  |  |  |  |  |  |  |  |
| llvm | .ll |  |  |  |  |  |  |  |  |
| logtalk | .lgt |  |  |  |  |  |  |  |  |
| lua | .lua | .wlua |  |  |  |  |  |  |  |
| make | .mak | Makefile | makefile | Makefile. | GNUmakefile |  |  |  |  |
| mako | .mao |  |  |  |  |  |  |  |  |
| maql | .maql |  |  |  |  |  |  |  |  |
| mason | .mhtml | .mc | .mi | autohandler | dhandler |  |  |  |  |
| markdown | .md |  |  |  |  |  |  |  |  |
| modelica | .mo |  |  |  |  |  |  |  |  |
| modula2 | .def | .mod |  |  |  |  |  |  |  |
| moocode | .moo |  |  |  |  |  |  |  |  |
| mupad | .mu |  |  |  |  |  |  |  |  |
| mxml | .mxml |  |  |  |  |  |  |  |  |
| myghty | .myt | autodelegate |  |  |  |  |  |  |  |
| nasm | .asm | .ASM |  |  |  |  |  |  |  |
| newspeak | .ns2 |  |  |  |  |  |  |  |  |
| objdump | .objdump |  |  |  |  |  |  |  |  |
| objectivec | .m |  |  |  |  |  |  |  |  |
| objectivej | .j |  |  |  |  |  |  |  |  |
| ocaml | .ml | .mli | .mll | .mly |  |  |  |  |  |
| ooc | .ooc |  |  |  |  |  |  |  |  |
| perl | .pl | .pm |  |  |  |  |  |  |  |
| php | .php | .php(345) |  |  |  |  |  |  |  |
| postscript | .ps | .eps |  |  |  |  |  |  |  |
| pot | .pot | .po |  |  |  |  |  |  |  |
| pov | .pov | .inc |  |  |  |  |  |  |  |
| prolog | .prolog | .pro | .pl |  |  |  |  |  |  |
| properties | .properties |  |  |  |  |  |  |  |  |
| protobuf | .proto |  |  |  |  |  |  |  |  |
| py3tb | .py3tb |  |  |  |  |  |  |  |  |
| pytb | .pytb |  |  |  |  |  |  |  |  |
| python | .py | .pyw | .sc | SConstruct | SConscript | .tac |  |  |  |
| r | .R |  |  |  |  |  |  |  |  |
| rb | .rb | .rbw | Rakefile | .rake | .gemspec | .rbx | .duby |  |  |
| rconsole | .Rout |  |  |  |  |  |  |  |  |
| rebol | .r | .r3 |  |  |  |  |  |  |  |
| redcode | .cw |  |  |  |  |  |  |  |  |
| rhtml | .rhtml |  |  |  |  |  |  |  |  |
| rst | .rst | .rest |  |  |  |  |  |  |  |
| sass | .sass |  |  |  |  |  |  |  |  |
| scala | .scala |  |  |  |  |  |  |  |  |
| scaml | .scaml |  |  |  |  |  |  |  |  |
| scheme | .scm |  |  |  |  |  |  |  |  |
| scss | .scss |  |  |  |  |  |  |  |  |
| smalltalk | .st |  |  |  |  |  |  |  |  |
| smarty | .tpl |  |  |  |  |  |  |  |  |
| sourceslist | sources.list |  |  |  |  |  |  |  |  |
| splus | .S | .R |  |  |  |  |  |  |  |
| sql | .sql |  |  |  |  |  |  |  |  |
| sqlite3 | .sqlite3-console |  |  |  |  |  |  |  |  |
| squidconf | squid.conf |  |  |  |  |  |  |  |  |
| ssp | .ssp |  |  |  |  |  |  |  |  |
| tcl | .tcl |  |  |  |  |  |  |  |  |
| tcsh | .tcsh | .csh |  |  |  |  |  |  |  |
| tex | .tex | .aux | .toc |  |  |  |  |  |  |
| text | .txt |  |  |  |  |  |  |  |  |
| v | .v | .sv |  |  |  |  |  |  |  |
| vala | .vala | .vapi |  |  |  |  |  |  |  |
| vbnet | .vb | .bas |  |  |  |  |  |  |  |
| velocity | .vm | .fhtml |  |  |  |  |  |  |  |
| vim | .vim | .vimrc |  |  |  |  |  |  |  |
| xml | .xml | .xsl | .rss | .xslt | .xsd | .wsdl |  |  |  |
| xquery | .xqy | .xquery |  |  |  |  |  |  |  |
| xslt | .xsl | .xslt |  |  |  |  |  |  |  |
| yaml | .yaml | .yml |  |  |  |  |  |  |  |

### Arpars boolean argument treatment - From [Codemia](https://codemia.io/knowledge-hub/path/parsing_boolean_values_with_argparse)
````````````
<h3 id="6bea7ebd390bd64ef0a32f9ffef5173a">crawlect.py</h3>  
`crawlect.py`

```python
#! /usr/bin/env python3

from pathlib import Path
from fnmatch import fnmatch
from math import inf

# Custom modules.
from scan import Scan
from format import Format
from output import Output

class Crawlect:
    """
    Client Crawlect class.
    Crawlect is a module intended to describe files from a given path and transcribe and save these into a single markdown file.
    """

    def __init__(self, path = None, output = None, output_prefix = None, output_suffix = None, recur = True, depth = inf, crawlectignore = None, gitignore = True, dockerignore = True, excl_pat_li = [], excl_fil_li = [], excl_ext_li = [], excl_dir_li = [], excl_fil_wr = [], excl_ext_wr = [], excl_dir_wr = [], incl_fil_li = [], incl_ext_li = [], incl_dir_li = [], incl_fil_wr = [], incl_ext_wr = [], incl_dir_wr = [], xenv = True, tree = True):

        # Store the class arguments for __repr__.
        self.args = dict()

        self.path = path
        self.args["path"] = self.path
        self.output = output
        self.args["output"] = self.output
        self.output_prefix = output_prefix
        self.args["output_prefix"] = self.output_prefix
        self.output_suffix = output_suffix
        self.args["output_suffix"] = self.output_suffix
        self.recur = recur
        self.args["recur"] = self.recur
        self.depth = depth
        self.args["depth"] = self.depth

        # Ignore files handling.
        self.crawlectignore = crawlectignore
        self.args["crawlectignore"] = self.crawlectignore
        self.gitignore = gitignore
        self.args["gitignore"] = self.gitignore
        self.dockerignore = dockerignore
        self.args["dockerignore"] = self.dockerignore
        self.mergedIgnore = []

        # Files and xtensions inclusion/exclusions parameters.
        self.excl_pat_li = excl_pat_li
        self.args["excl_pat_li"] = self.excl_pat_li
        self.excl_fil_li = excl_fil_li
        self.args["excl_fil_li"] = self.excl_fil_li
        self.excl_ext_li = excl_ext_li
        self.args["excl_ext_li"] = self.excl_ext_li
        self.excl_dir_li = excl_dir_li
        self.args["excl_dir_li"] = self.excl_dir_li
        self.incl_fil_li = incl_fil_li
        self.args["incl_fil_li"] = self.incl_fil_li
        self.incl_ext_li = incl_ext_li
        self.args["incl_ext_li"] = self.incl_ext_li
        self.incl_dir_li = incl_dir_li
        self.args["incl_dir_li"] = self.incl_dir_li
        self.excl_fil_wr = excl_fil_wr
        self.args["excl_fil_wr"] = self.excl_fil_wr
        self.excl_ext_wr = excl_ext_wr
        self.args["excl_ext_wr"] = self.excl_ext_wr
        self.excl_dir_wr = excl_dir_wr
        self.args["excl_dir_wr"] = self.excl_dir_wr
        self.incl_fil_wr = incl_fil_wr
        self.args["incl_fil_wr"] = self.incl_fil_wr
        self.incl_ext_wr = incl_ext_wr
        self.args["incl_ext_wr"] = self.incl_ext_wr
        self.incl_dir_wr = incl_dir_wr
        self.args["incl_dir_wr"] = self.incl_dir_wr

        # Advanced features parameters.
        self.xenv = xenv
        self.args["xenv"] = self.xenv
        self.tree = tree
        self.args["tree"] = self.tree

        # File overwrite denied by default.
        self.writeRight = "x"

        self.validateParam()

        self.warmUp()

        self.initServices()

        self.processIgnoreFiles()

        self.generatePathList()

    # To be enhanced. State patern for interactive/module mode?
    def validateParam(self):
        """Validate attributes and regenerate dynamic attributes."""

        # Max depth adaptation if recur is False.
        if not self.recur:
            self.depth = 1

        # Interactive mode.
        if __name__ == "__main__":

            while self.path is None:
                self.path = input(f"\n# Missing argument #\n{type(self).__name__} require a path to crawl. Please enter the desired path (e.g.: '.') or [Ctrl]+[C] then [Enter] to abort.\n")

            while not Path(self.path).exists():
                self.path = input(f"\n# Path error #\n{type(self).__name__} could not find {repr(self.path)}, please enter the path to crawl.\n")

            while self.output is None and self.output_prefix is None:
                print(f"\n# Missing argument #\n{type(self).__name__} require an output file-name for static output file-name (e.g.: './description.md')\nOR\nan output prefix and output suffix for unique output file-name (e.g.: './descript' as prefix, and '.md' as suffix), this will create a path similar to: './descript-202506041010-g5ef9h.md'")
                while True:
                    _ = input("Please choose between 'static' and 'unique', or [Ctrl]+[C] then [Enter] to abort.\n").lower()
                    if _ == "static":
                        while self.output is None or not self.output:
                            self.output = input("Please enter a static output file-name, e.g.: './output.md' or [Ctrl]+[C] then [Enter] to abort.\n")
                        break
                    elif _ == "unique":
                        while self.output_prefix is None or not self.output_prefix:
                            self.output_prefix = input("Please enter a prefix, e.g.: './output' or [Ctrl]+[C] then [Enter] to abort.\n")
                        while self.output_suffix is None:
                            self.output_suffix = input("Please enter a suffix, e.g.: '.md' (suffix can be empty) or [Ctrl]+[C] then [Enter] to abort.\n")
                        break
                    else:
                        continue

            if self.output is not None:
                if Path(self.output).exists():
                        print(f"\n# File overwrite #\n{type(self).__name__} is about to overwrite {repr(self.output)}. Its content will be lost!")
                        while True:
                            _ = input("Please choose between 'proceed' and 'change', or [Ctrl]+[C] then [Enter] to abort.\n").lower()
                            if _ == "proceed":
                                # File overwrite permission granted upon request in CLI mode.
                                self.writeRight = "w"
                                break
                            elif _ == "change":
                                self.output = None
                                self.output_prefix = None
                                self.validate()
                                break
                            else:
                                continue

        # Module mode.
        else:

            # File overwrite denied in module mode.
            self.writeRight = "x"

            if self.output is not None:
                if Path(self.output).exists():
                    raise IOError(f"\n# Permission error #\n{type(self).__name__} do not allow file {repr(self.output)} to be overwrited in module mode. Please errase the file first if you want to keep this output path.")

            validationMessage = ""
            if self.path is None:
                validationMessage += "- A path to crawl, e.g.: path = '.'\n"
            elif not Path(self.path).exists():
                validationMessage += f"A valid path to crawl, {self.path} cannot be found.\n"
            if self.output is None and self.output_prefix is None:
                validationMessage += "- An output file-name for static output file-name (e.g.: --output = './description.md')\nOR\nan output prefix and output suffix for unique output file-name (e.g.: --output_prefix = './descript', --output_suffix = '.md' as suffix), this will create a path similar to: './descript-202506041010-g5ef9h.md'\n"
            if validationMessage:
                raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires:\n{validationMessage}Got: {self}")

    def warmUp(self):
        """Set needed variable for Crawlect service init phase"""
        try:
            self.pathObj = Path(self.path)
        except:
            print(f"Error: on {type(self).__name__}:\ncould not set its paths from path attribute.")
            raise

        try:
            self.title = self.pathObj.resolve().name
        except:
            print(f"Error: on {type(self).__name__}:\ncould not set its title.")
            raise

    def initServices(self):
        """Build Crawlect services"""
        try:
            self.scanService = Scan(self)
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Scan service.")
            raise

        try:
            self.formatService = Format() # Format does not take Crawlect instance as parameter.
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Format service.")
            raise

        try:
            self.outputService = Output(self)
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Output service.")
            raise

    def processIgnoreFiles(self):
        """Check for ignore files settings and fetch ignore list from these."""
        if self.crawlectignore is not None:
            self.mergedIgnore.extend(self.getIgnoreListFromFile(self.crawlectignore))

        if self.gitignore and Path(self.path + "/.gitignore").exists():
            self.mergedIgnore.extend(self.getIgnoreListFromFile(self.path + "/.gitignore"))
            self.mergedIgnore.append(".git")

        if self.dockerignore and Path(self.path + "/.dockerignore").exists():
            self.mergedIgnore.extend(self.getIgnoreListFromFile(self.path + "/.dockerignore"))

        # Get unique ignore path values.
        self.mergedIgnore = list(set(self.mergedIgnore))

    def generatePathList(self):
        """Prepare the path list which will be treated and written in output file."""
        try:
            self.files = self.scanService.listPathIn()
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and proceed to paths listing.")
            raise

    def getTitle(self):
        """Simply returns path to crawl's name"""
        return self.title

    def getIgnoreListFromFile(self, file = None):
        """Try to get ignore file and parse its ignore rules in a list."""

        # Does not support advanced .gitignore syntax such as the "!" for not ignoring at the moment. It will probably not be handled here but in the *Scan* class thought.

        ignoreList = []
        try:
            with open(file) as ignoreFile:
                for line in ignoreFile.read().splitlines():
                     if line and "#" not in line:
                        ignoreList.append(line)
        except Exception as error:
            print(f"\n!! - {type(error).__name__}:\n{type(self).__name__} could not process getIgnoreListFromFile({repr(file)}): {error}")
        return ignoreList

    # Assess if this should be sent to a common class ("Filter" class ?).
    def isPathIgnored(self, path):
        """Check if path match any .gitignore pattern or path include/exclude list parameter item."""

        # Does not support advanced .gitignore syntax such as the "!" for not ignoring at the moment.

        for ignored in self.mergedIgnore:
            if fnmatch(path, ignored):
                return True

        # Check if path is in path ignore list parameter.
        for excludedPath in self.excl_pat_li:
            if path == Path(excludedPath):
                return True

        return False

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"


####################
# INTERACTIVE MODE #
####################

if __name__ == "__main__":

    import argparse
    import traceback

    class BooleanAction(argparse.Action):
        """
        This method converts argpars argument string to a boolean (e.g.: "yes" => True).
        From [Codemia](https://codemia.io/knowledge-hub/path/parsing_boolean_values_with_argparse)
        """

        def __call__(self, parser, namespace, values, option_string = None):
            if values.lower() in ("yes", "y", "true", "t", "1"):
                setattr(namespace, self.dest, True)
            elif values.lower() in ("no", "n", "false", "f", "0"):
                setattr(namespace, self.dest, False)
            else:
                raise argparse.ArgumentTypeError(f"Unsupported boolean value: {values}")

    try:
        # Parameters.
        parser = argparse.ArgumentParser(
            description = "Crawlect crawl a given path to list and describe all files on a single markdown file.",
            epilog = "Filtering rules allow you to forcibly include or exclude certain directories, files names or file extensions. All files will be listed if there are no rules. Inclusion overrules exclusion on same caracteristics and file-name rules takes precedence against extension rules."
        )

        parser.add_argument(
            "-p", "--path", "--path_to_crawl",
            type = str,
            default = ".",
            help = "Path to crawl (default is current folder \".\").")

        parser.add_argument(
            "-o", "--output", "--output_file",
            type = str,
            default = None,
            help = "Output markdown digest file (default is None).")

        parser.add_argument(
            "-op", "--output_prefix", "--output_file_prefix",
            type = str,
            default = "description",
            help = "Output markdown digest file prefix ('description' by default) associated with --output_suffix can be use as an alternative to '--output' argument to generate a unique file-name (e.g.: --output_prefix = './descript', output_suffix = '.md' will create './descript-202506041010-g5ef9h.md').")

        parser.add_argument(
            "-os", "--output_suffix", "--output_file_suffix",
            type = str,
            default = ".md",
            
            help = "Output markdown digest file prefix ('.md' by default) associated with --output_prefix can be use as an alternative to '--output' argument to generate a unique file-name (e.g.: --output_prefix = './descript', output_suffix = '.md' will create './descript-202506041010-g5ef9h.md').")

        parser.add_argument(
            "-r", "--recur", "--recursive_crawling",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Enable recursive crawling (default is True).")

        parser.add_argument(
            "-d", "--depth", "--recursive_crawling_depth",
            type = int,
            default = inf,
            help = "Scan depth limit (default is infinite).")

        # Ignore files handling.
        parser.add_argument(
            "-crawlig", "--crawlectignore", "--crawlectignore_use",
            type = str,
            default = None,
            help = "Use custom file as Crawlect exclusion rules (default is None).")

        parser.add_argument(
            "-gitig", "--gitignore", "--gitignore_use",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Use .gitignore exclusion rules if exist (default is True).")

        parser.add_argument(
            "-dokig", "--dockerignore", "--dockerignore_use",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Use .dockerignore exclusion rules if exist (default is True).")

        # Files and xtensions inclusion/exclusions parameters.
        parser.add_argument(
            "-xpl", "--excl_pat_li", "--excluded_paths_from_listing",
            nargs = "*",
            default = [],
            help = "List of paths to exclude from listing (e.g.: ./messy_folder/, ./album/vacation_56.png).")

        parser.add_argument(
            "-xfl", "--excl_fil_li", "--excluded_files_from_listing",
            nargs = "*",
            default = [],
            help = "List of files to exclude from listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-xel", "--excl_ext_li", "--excluded_xtensions_from_listing",
            nargs = "*",
            default = [],
            help = "List of file extensions to exclude from listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdl", "--excl_dir_li", "--excluded_directories_from_listing",
            nargs = "*",
            default = [],
            help = "List of directories to exclude from listing (e.g.: bin, render).")

        parser.add_argument(
            "-ifl", "--incl_fil_li", "--include_files_for_listing",
            nargs = "*",
            default = [],
            help = "List of files to include for listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iel", "--incl_ext_li", "--include_xtensions_for_listing",
            nargs = "*",
            default = [],
            help = "List of file extensions to include for listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idl", "--incl_dir_li", "--include_directories_for_listing",
            nargs = "*",
            default = [],
            help = "List of directories to include for listing (e.g.: bin, render).")

        parser.add_argument(
            "-xfw", "--excl_fil_wr", "--excluded_files_from_writing",
            nargs = "*",
            default = [],
            help = "List of files to exclude from writing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-xew", "--excl_ext_wr", "--excluded_xtensions_from_writing",
            nargs = "*",
            default = [],
            help = "List of file extensions to exclude from writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdw", "--excl_dir_wr", "--excluded_directories_from_writing",
            nargs = "*",
            default = [],
            help = "List of directories to exclude from writing (e.g.: bin, render).")

        parser.add_argument(
            "-ifw", "--incl_fil_wr", "--include_files_for_writing",
            nargs = "*",
            default = [],
            help = "List of files to include for writing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iew", "--incl_ext_wr", "--include_xtensions_for_writing",
            nargs = "*",
            default = [],
            help = "List of file extensions to include for writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idw", "--incl_dir_wr", "--include_directories_for_writing",
            nargs = "*",
            default = [],
            help = "List of directories to include for writing (e.g.: bin, render).")

        # Advanced features parameters.
        parser.add_argument(
            "-xen", "--xenv", "--sanitize_env_variables",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Sanitize .env variables to mitigate sensitive info leak risk (default is True).")

        parser.add_argument(
            "-tre", "--tree", "--visualize_directory_tree",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Visualize directory tree in the output file (default is True).")

        args = parser.parse_args()

        crawlect = Crawlect(path = args.path, output = args.output, output_prefix = args.output_prefix, output_suffix = args.output_suffix, recur = args.recur, depth = args.depth, excl_pat_li = args.excl_pat_li, excl_fil_li = args.excl_fil_li, excl_ext_li = args.excl_ext_li, excl_dir_li = args.excl_dir_li, excl_fil_wr = args.excl_fil_wr, excl_ext_wr = args.excl_ext_wr, excl_dir_wr = args.excl_dir_wr, incl_fil_li = args.incl_fil_li, incl_ext_li = args.incl_ext_li, incl_dir_li = args.incl_dir_li, incl_fil_wr = args.incl_fil_wr, incl_ext_wr = args.incl_ext_wr, incl_dir_wr = args.incl_dir_wr, crawlectignore = args.crawlectignore, gitignore = args.gitignore, dockerignore = args.dockerignore,xenv = args.xenv, tree = args.tree)

        # Launch output file composition
        crawlect.outputService.compose()

        # Confirm.
        print(f"\n{type(crawlect.outputService).__name__} processed {repr(crawlect.getTitle())} and stored description in {repr(crawlect.outputService.currentOutputName)}.")

    except KeyboardInterrupt:
        print("Interupted by user.")

    except Exception as error:
        print(f"\nUnexpected {type(error).__name__}:\n{error}\n")

        # Debug.
        lines = traceback.format_tb(error.__traceback__)
        for line in lines:
            print(line)
```
<h3 id="b93cb4ee570a6381a51faf63b1b83e8b">format.py</h3>  
`format.py`

```python
import json
import hashlib
from pathlib import Path

class Format:
    """
    La classe prend en entrée un chemin de fichier path fourni par la classe scan.
    Va identifier le type de fichier et le placer dans un codbox

    """
    # attribut de classe
    counter_idmd = -1
    def __init__(self):

        try:

            with open("languages.json", "rt") as f:
                self.languages = json.load(f)
        except:
            print("Tables de mapage introuvables")
        
        

    def insertCodebox(self, file):
        """
        cette méthode prends en entrée un chemin de fichier avec son extention fourni par searchType()
        et retourne une variable string avec tous le code corresponding dans un codbox
        """

        extention = self.searchType(file)
        if extention == None:
            return None
        bloc = "`"
        with open(file, "rt") as f:
            code = f.read()

        # sources des commandes trouvées pour la gestion des textes : https://www.w3schools.com/python/python_ref_string.asp
        # Afficher un .env n'est pas souhaitable il faut masquer les valeurs
        if file.name == ".env":
            contenu = ""
            for ligne in code.splitlines():
                newlinge = ligne.lstrip(" ")

                # remplacement des valeurs des variables d'environnement par une valeur générique
                if newlinge and newlinge[0] != "#":
                    newlinge = newlinge.split("=")
                    variable_env = newlinge[0]
                    newlinge[1] = f"YourValueFor_{variable_env.lower()}"
                    newlinge = "=".join(newlinge)

                contenu += newlinge + "\n"
            # print(contenu)
            return f"{3*bloc}{extention}\n{contenu}\n{3*bloc}"

        # vérifie que l'extention est pas du markdown car ce type de fichier dispose de codebox
        elif extention != "markdown":
            res = f"{3*bloc}{extention}\n{code}\n{3*bloc}"
            # print(res)
            # print("")
            return res

        else:
            counter = 1
            maxrep = 1

            for l in range(1, len(code) - 1):
                if code[l] == code[l + 1] == "`":
                    counter += 1

                else:
                    if counter > maxrep:
                        maxrep = counter
                        counter = 1

            if counter > maxrep:
                maxrep = counter

            if maxrep >= 3:
                maxrep += 1
                res = f"{maxrep*bloc}{extention}\n{code}\n{maxrep*bloc}"
                # print(res)
                # print("")
                return res

            else:
                res = f"{3*bloc}{extention}\n{code}\n{3*bloc}"
                # print(res)
                # print("")
                return res
            

    def searchType(self, file):
        """
        Prend le chemin d'un fichier et retourne le type de fichier à inscrire dans la codebox
        """

        # recherche sur le nom de fichier
        if file.name in self.languages:
            # print(f"voici le fichier trouvée : {self.languages[file.name]}")
            return self.languages[file.name]

        elif file.suffix in self.languages:
            # print(f"voici l'extention trouvée : {self.languages[file.suffix]}")
            return self.languages[file.suffix]

        else:
            # print(f"fichier introuvés pour {file}")
            return None
        

    def makeTreeMd(self, chemin,  chemin_ignorer= [], deep = 20, level=0, racine = True):
        if level >= deep + 1 :
            return ""
        
        
        if chemin.name in chemin_ignorer:
            self.counter_idmd -= 1
            return ""
        
        if chemin.is_file in chemin_ignorer:
            self.counter_idmd -= 1
            return ""
        
        
        tree = ""
        indentation = "    "*level

        #print(f"{indentation}|__ {chemin.name}{fin}")
        if level == 0 and racine:
            self.counter_idmd = -1
            tree += f"- **{chemin.resolve().name}/**  \n"
        
        idmd = str(self.counter_idmd) 
        
        if level>0:
            if chemin.is_file():
                chemin_id = hashlib.md5(str(chemin.resolve()).encode()).hexdigest()
                tree += f"{indentation}- [{chemin.name}](#{chemin_id})  \n"
            if chemin.is_dir():
                tree += f"{indentation}- `{chemin.name}/`  \n"

        if chemin.is_dir():
            fichier_iterables = chemin.iterdir()
            fichier_liste = []
            dossier_liste = []
            for item in fichier_iterables:
                if item.is_file():
                    fichier_liste.append(item)
                if item.is_dir():
                    dossier_liste.append(item)
            
            dossiers = sorted(dossier_liste)
            fichiers = sorted(fichier_liste)
              
            for fichier in fichiers:
                try:
                #appel récursif 
                    self.counter_idmd += 1
                    tree += self.makeTreeMd(fichier, chemin_ignorer,deep,level +1, False)
                except PermissionError:
                    tree += ""
            for dossier in dossiers:
                try:
                    self.counter_idmd += 1
                    tree += self.makeTreeMd(dossier, chemin_ignorer,deep, level +1, False)

                except PermissionError:
                    
                    tree += ""
        #print(tree)
        return tree

        




```
<h3 id="7bcc248ab64f1e00243d36895ca6820f">languages.json</h3>  
`languages.json`

```json

{
  ".abap": "abap",
  ".ada": "ada",
  ".adb": "ada",
  ".ads": "ada",
  ".ahk": "ahk",
  ".ahkl": "ahk",
  ".htaccess": "apacheconf",
  "apache.conf": "apacheconf",
  "apache2.conf": "apacheconf",
  ".applescript": "applescript",
  ".as": "as",
  ".asy": "asy",
  ".bash": "bash",
  ".ebuild": "bash",
  ".eclass": "bash",
  ".env.example": "bash",
  ".env.local": "bash",
  ".env": "bash",
  ".ksh": "bash",
  ".sh": "bash",
  ".bat": "bat",
  ".cmd": "bat",
  ".befunge": "befunge",
  ".bmx": "blitzmax",
  ".boo": "boo",
  ".b": "brainfuck",
  ".bf": "brainfuck",
  ".c": "c", ".h": "c",
  ".cfc": "cfm",
  ".cfm": "cfm",
  ".cfml": "cfm",
  ".spt": "cheetah",
  ".tmpl": "cheetah",
  ".cl": "cl",
  ".el": "cl",
  ".lisp": "cl",
  ".clj": "clojure",
  ".cljs": "clojure",
  ".cmake": "cmake",
  "CMakeLists.txt": "cmake",
  ".coffee": "coffeescript",
  ".sh-session": "console",
  "control": "control",
  ".c++": "cpp",
  ".cc": "cpp",
  ".cpp": "cpp",
  ".cxx": "cpp",
  ".h++": "cpp",
  ".hh": "cpp",
  ".hpp": "cpp",
  ".hxx": "cpp",
  ".pde": "cpp",
  ".cs": "csharp",
  ".css": "css",
  ".feature": "cucumber",
  ".pxd": "cython",
  ".pxi": "cython",
  ".pyx": "cython",
  ".d": "d",
  ".di": "d",
  ".pas": "delphi",
  ".diff": "diff",
  ".patch": "diff",
  "Dockerfile.": "dockerfile",
  "Dockerfile": "dockerfile",
  ".darcspatch": "dpatch",
  ".dpatch": "dpatch",
  ".duel": "duel",
  ".jbst": "duel",
  ".dyl": "dylan",
  ".dylan": "dylan",
  ".erb": "erb",
  ".erl-sh": "erl",
  ".erl": "erlang",
  ".hrl": "erlang",
  ".evoque": "evoque",
  ".factor": "factor",
  ".flx": "felix",
  ".flxh": "felix",
  ".f": "fortran",
  ".f90": "fortran",
  ".s": "gas",
  ".kid": "genshi",
  ".gitignore": "gitignore",
  ".frag": "glsl",
  ".geo": "glsl",
  ".vert": "glsl",
  ".plot": "gnuplot",
  ".plt": "gnuplot",
  ".go": "go",
  ".(1234567)": "groff",
  ".man": "groff",
  ".haml": "haml",
  ".hs": "haskell",
  ".htm": "html",
  ".html": "html",
  ".xhtml": "html",
  ".hx": "hx",
  ".hy": "hybris",
  ".hyb": "hybris",
  ".cfg": "ini",
  ".conf": "ini",
  ".editorconfig": "ini",
  ".flake8": "ini",
  ".ini": "ini",
  ".npmrc": "ini",
  ".io": "io",
  ".ik": "ioke",
  ".weechatlog": "irc",
  ".jade": "jade",
  ".java": "java",
  ".js": "js",
  ".babelrc": "json",
  ".eslintrc": "json",
  ".json": "json",
  ".json5": "json",
  ".prettierrc": "json",
  ".jsp": "jsp",
  ".lhs": "lhs",
  ".ll": "llvm",
  ".lgt": "logtalk",
  ".lua": "lua",
  ".wlua": "lua",
  ".mak": "make",
  "GNUmakefile": "make",
  "Makefile.": "make",
  "Makefile": "make",
  "makefile": "make",
  ".mao": "mako",
  ".maql": "maql",
  ".md": "markdown",
  ".mc": "mason",
  ".mhtml": "mason",
  ".mi": "mason",
  "autohandler": "mason",
  "dhandler": "mason",
  ".mo": "modelica",
  ".def": "modula2",
  ".mod": "modula2",
  ".moo": "moocode",
  ".mu": "mupad",
  ".mxml": "mxml",
  ".myt": "myghty",
  "autodelegate": "myghty",
  ".asm": "nasm",
  ".ASM": "nasm",
  ".ns2": "newspeak",
  ".objdump": "objdump",
  ".m": "objectivec",
  ".j": "objectivej",
  ".ml": "ocaml",
  ".mli": "ocaml",
  ".mll": "ocaml",
  ".mly": "ocaml",
  ".ooc": "ooc",
  ".pl": "perl",
  ".pm": "perl",
  ".php(345)": "php",
  ".php": "php",
  ".eps": "postscript",
  ".ps": "postscript",
  ".po": "pot",
  ".pot": "pot",
  ".inc": "pov",
  ".pov": "pov",
  ".pro": "prolog",
  ".prolog": "prolog",
  ".properties": "properties",
  ".proto": "protobuf",
  ".py3tb": "py3tb",
  ".pytb": "pytb",
  ".py": "python",
  ".pyw": "python",
  ".sc": "python",
  ".tac": "python",
  "SConscript": "python",
  "SConstruct": "python",
  ".R": "r",
  ".duby": "rb",
  ".gemspec": "rb",
  ".rake": "rb",
  ".rb": "rb",
  ".rbw": "rb",
  ".rbx": "rb",
  "Rakefile": "rb",
  ".Rout": "rconsole",
  ".r": "rebol",
  ".r3": "rebol",
  ".cw": "redcode",
  ".rhtml": "rhtml",
  ".rest": "rst",
  ".rst": "rst",
  "Vagrantfile": "ruby",
  ".sass": "sass",
  ".scala": "scala",
  ".scaml": "scaml",
  ".scm": "scheme",
  ".scss": "scss",
  ".st": "smalltalk",
  ".tpl": "smarty",
  "sources.list": "sourceslist",
  ".S": "splus",
  ".sql": "sql",
  ".sqlite3-console": "sqlite3",
  "squid.conf": "squidconf",
  ".ssp": "ssp",
  ".tcl": "tcl",
  ".csh": "tcsh",
  ".tcsh": "tcsh",
  ".aux": "tex",
  ".tex": "tex",
  ".toc": "tex",
  ".log": "text",
  ".txt": "text",
  "requirements.txt": "text",
  ".toml": "toml",
  "Pipfile.lock": "toml",
  "Pipfile": "toml",
  "pyproject.toml": "toml",
  ".sv": "v",
  ".v": "v",
  ".vala": "vala",
  ".vapi": "vala",
  ".bas": "vbnet",
  ".vb": "vbnet",
  ".fhtml": "velocity",
  ".vm": "velocity",
  ".vim": "vim",
  ".vimrc": "vim",
  ".rss": "xml",
  ".wsdl": "xml",
  ".xml": "xml",
  ".xsd": "xml",
  ".xslt": "xml",
  ".xquery": "xquery",
  ".xqy": "xquery",
  ".xsl": "xslt",
  ".yaml": "yaml",
  ".yarnrc": "yaml",
  ".yml": "yaml"
}
```
<h3 id="773017d6f93fc69b8fb7fd5a853427ef">output.py</h3>  
`output.py`

```python
#! /usr/bin/env python3

from pathlib import Path
from datetime import datetime
from random import choices
import string
import hashlib

class Output:
    """
    Output class provide standard Crawlec output features.
    It require and only accept one instance of Crawlect as argument.
    """

    __rand_filename_char_list = string.ascii_lowercase + string.digits

    def __init__(self, crawler):

        # Validate.
        if type(crawler).__name__ != "Crawlect":
            raise TypeError(f"{type(self).__name__} class require and only accept one instance of Crawlect as argument.")

        # Store the class arguments for __repr__.
        self.args = dict()

        self.crawler = crawler
        self.args["crawler"] = self.crawler = crawler

        self.currentOutputName = ""
        self.composition = ()

    def compose(self):
        """Compose output file."""

        date = datetime.now()
        self.currentOutputName = self.standardOutputName()

        # Early version.
        with open(self.currentOutputName, self.crawler.writeRight) as outputFile:

            # Title
            outputFile.write(f"# {self.crawler.getTitle()}\n{str(date.year)}.{str("{:02d}".format(date.month))}.{str("{:02d}".format(date.day))} {str("{:02d}".format(date.hour))}:{str("{:02d}".format(date.minute))}\n\nGenerated with {type(self.crawler).__name__}.\n\n")

            # Directory tree
            if self.crawler.tree:
                exclude = self.crawler.excl_dir_li
                exclude.append(self.currentOutputName)
                outputFile.write(f"## File structure\n\nDirectory tree.\n\n{self.crawler.formatService.makeTreeMd(self.crawler.pathObj, chemin_ignorer = exclude, deep = self.crawler.depth)}\n\n")

            # Files list

            # sort file
            sorted_files = self.crawler.files
            sorted_files.sort(key = lambda p: (p.parent, p.name))

            outputFile.write("## Files:\n\n")
            for file in sorted_files:

                chemin_id = hashlib.md5(str(file.resolve()).encode()).hexdigest()

                if file.is_file() and str(file) != self.currentOutputName:
                    outputFile.write(f"<h3 id=\"{chemin_id}\">{file.name}</h3>  \n")
                    outputFile.write(f"`{file}`\n\n")
                    if self.isFileToInclude(file):
                        try:
                            content = self.crawler.formatService.insertCodebox(file)
                            if not content is None:
                                outputFile.write(self.crawler.formatService.insertCodebox(file))

                        except Exception as error:
                            print(f"\n!! - {type(error).__name__}:\n{type(self).__name__} could not create codebox from {repr(file)}: {error}")
                    outputFile.write("\n")

    def standardOutputName(self):
        """Return standard output file name if no filename specified."""

        if self.crawler.output is None:
            now = datetime.now()
            return f"{self.crawler.output_prefix}-{self.yearmodahs()}-{"".join(choices(self.__rand_filename_char_list, k = 6))}{self.crawler.output_suffix}"
        else:
            return self.crawler.output

    def yearmodahs(self, date = datetime.now()):
        """Return givent date as yearmoda plus hours and seconds string."""

        return str(date.year) + str("{:02d}".format(date.month)) + str("{:02d}".format(date.day)) + str("{:02d}".format(date.hour)) + str("{:02d}".format(date.minute)) + str("{:02d}".format(date.second))

    # Almost identical methode in Scan and Output classes. Assess if this should be sent to a common class ("Filter" class ?).
    def isFileToInclude(self, path):
        """
        Filter file `path` according to filtering rules.
        All files pass if there are no rules.
        Inclusion overrules exclusion.
        File-name rules takes precedence against extension rules.
        """

        # Ignore files such as `.gitignore` rules above all.
        if self.crawler.isPathIgnored(path):
            return False

        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_ext_wr == [] and self.crawler.excl_fil_wr == [] and self.crawler.incl_ext_wr == [] and self.crawler.incl_fil_wr == []:
            return True

        # Forcibly included by file-name always wins:
        if path.name in self.crawler.incl_fil_wr:
            return True

        # Forcibly included by extension and not excluded by file-name wins:
        if path.suffix in self.crawler.incl_ext_wr and path.name not in self.crawler.excl_fil_wr:
            return True

        # Forcibly excluded by extension looses if not saved by file-name inclusion:
        if path.suffix in self.crawler.excl_ext_wr and path.name not in self.crawler.incl_fil_wr:
            return False

        # Forcibly excluded by file-name always looses:
        if path.name in self.crawler.excl_fil_wr:
            return False

        # Is neither forcibly included or excluded but an extension or file inclusion is overruling:
        if self.crawler.incl_ext_wr != [] or self.crawler.incl_fil_wr != []:
            return False

        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"
```
<h3 id="ff6c8e5c9d5f8eff49a0cac54a8b5bbd">scan.py</h3>  
`scan.py`

```python
#! /usr/bin/env python3

from pathlib import Path

class Scan:
    """
    Scan class contains Crawlect directories tree scan utilities.
    It require and only accept one instance of Crawlect as argument.
    """

    def __init__(self, crawler = None):

        # Validate.
        if type(crawler).__name__ != "Crawlect":
            raise TypeError(f"{type(self).__name__} class require and only accept one instance of Crawlect as argument.")

        # Store the class arguments for __repr__.
        self.args = dict()

        self.crawler = crawler
        self.args["crawler"] = self.crawler

    def listPathIn(self, path = None, depth = None, files = None):
        """Append all eligible paths from `crawler.path` as Path object in a list and return it."""
        if files is None:
            files = []

        if depth is None:
            depth = self.crawler.depth

        if path is None:
            path = self.crawler.pathObj

        for candidatePath in path.iterdir():
            try:
                if candidatePath.is_file() and self.isFileToInclude(candidatePath):
                    files.append(candidatePath)
                elif candidatePath.is_dir() and self.crawler.recur and depth >= 1 and self.isDirToInclude(candidatePath):
                    files.append(candidatePath)
                    self.listPathIn(path = candidatePath, depth = depth-1, files = files)
            except PermissionError as err:
                print(f"\n!! - {type(err).__name__} :\n{type(self) .__name__} Could not list path {repr(candidatePath)}: {err} ")
        return files

    # Almost identical methode in Scan and Output classes. Assess if this should be sent to a common class ("Filter" class ?).
    def isFileToInclude(self, path):
        """
        Filter file `path` according to filtering rules.
        All files pass if there are no rules.
        Inclusion overrules exclusion.
        File-name rules takes precedence against extension rules.
        """

        # Always exclude output file.
        if str(path) == self.crawler.output:
            return False

        # Ignore files such as `.gitignore` rules above all.
        if self.crawler.isPathIgnored(path):
            return False

        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_ext_li == [] and self.crawler.excl_fil_li == [] and self.crawler.incl_ext_li == [] and self.crawler.incl_fil_li == []:
            return True

        # Forcibly included by file-name always wins:
        if path.name in self.crawler.incl_fil_li:
            return True

        # Forcibly included by extension and not excluded by file-name wins:
        if path.suffix in self.crawler.incl_ext_li and path.name not in self.crawler.excl_fil_li:
            return True

        # Forcibly excluded by extension looses if not saved by file-name inclusion:
        if path.suffix in self.crawler.excl_ext_li and path.name not in self.crawler.incl_fil_li:
            return False

        # Forcibly excluded by file-name always looses:
        if path.name in self.crawler.excl_fil_li:
            return False

        # Is neither forcibly included or excluded but an extension or file inclusion is overruling:
        if self.crawler.incl_ext_li != [] or self.crawler.incl_fil_li != []:
            return False

        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True

    # Almost identical methode in Scan and Output classes. Assess if this should be sent to a common class ("Filter" class ?).
    def isDirToInclude(self, path):
        """
        Filter directory `path` according to filtering rules.
        All directories pass if there are no rules.
        Inclusion overrules exclusion.
        """

        # Ignore files such as `.gitignore` rules above all.
        if self.crawler.isPathIgnored(path):
            return False

        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_dir_li == [] and self.crawler.incl_dir_li == []:
            return True

        # Is forcibly included:
        if path.name in self.crawler.incl_dir_li:
            return True

        # Is forcibly excluded:
        if path.name in self.crawler.excl_dir_li:
            return False

        # Is neither forcibly included or excluded but a directory inclusion is overruling:
        if self.crawler.incl_dir_li != []:
            return False

        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"
```
<h3 id="1bd718d1d601e0cf83b445d1c902e1a4">.gitignore</h3>  
`.idea\.gitignore`

```gitignore
# Default ignored files
/shelf/
/workspace.xml

```
<h3 id="3e6fa50ac5b862a61c578be7a1137ea2">misc.xml</h3>  
`.idea\misc.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="Black">
    <option name="sdkName" value="Python 3.12" />
  </component>
  <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.12" project-jdk-type="Python SDK" />
</project>
```
<h3 id="77620dde52ce244914a8459f52dcffb4">modules.xml</h3>  
`.idea\modules.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
      <module fileurl="file://$PROJECT_DIR$/.idea/crawlect.iml" filepath="$PROJECT_DIR$/.idea/crawlect.iml" />
    </modules>
  </component>
</project>
```
<h3 id="fdd4e0cf92465a832b219796ad4073e1">vcs.xml</h3>  
`.idea\vcs.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="VcsDirectoryMappings">
    <mapping directory="" vcs="Git" />
  </component>
</project>
```
<h3 id="99eb69626b3ce864a04eb3cbb6eb152b">profiles_settings.xml</h3>  
`.idea\inspectionProfiles\profiles_settings.xml`

```xml
<component name="InspectionProjectProfileManager">
  <settings>
    <option name="USE_PROJECT_PROFILE" value="false" />
    <version value="1.0" />
  </settings>
</component>
```
