# -*- coding: utf-8 -*-
"""
Script to generate data.js for Jukugo Master web application.
"""
import json

raw_data = [
    # ==========================================
    # MINGGU 1 (22 Kanji)
    # ==========================================
    {
        "week": 1,
        "kanji": "株",
        "onyomi": "シュ",
        "kunyomi": "かぶ",
        "meaning": "Saham, tunggul tanaman",
        "jukugo": [
            {
                "word": "株式",
                "furigana": "かぶしき",
                "romaji": "kabushiki",
                "meaning": "Saham / efek kepemilikan saham",
                "level": "N2",
                "example": "彼は株式会社を立ち上げた。",
                "example_reading": "かれはかぶしきがいしゃをたちあげた。",
                "example_meaning": "Dia mendirikan sebuah perseroan terbatas (PT)."
            },
            {
                "word": "株価",
                "furigana": "かぶか",
                "romaji": "kabuka",
                "meaning": "Harga saham",
                "level": "N2",
                "example": "東京市場で株価が急落した。",
                "example_reading": "とうきょうしじょうでかぶかがきゅうらくした。",
                "example_meaning": "Harga saham anjlok di pasar Tokyo."
            },
            {
                "word": "株主",
                "furigana": "かぶぬし",
                "romaji": "kabunushi",
                "meaning": "Pemegang saham",
                "level": "N2",
                "example": "来週、株主総会が開催される。",
                "example_reading": "らいしゅう、かぶぬしそうかいがかいさいされる。",
                "example_meaning": "Minggu depan, rapat umum pemegang saham akan diadakan."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "随",
        "onyomi": "ズイ",
        "kunyomi": "したが・う",
        "meaning": "Mengikuti, sesuka hati, sewaktu-waktu",
        "jukugo": [
            {
                "word": "随時",
                "furigana": "ずいじ",
                "romaji": "zuiji",
                "meaning": "Sewaktu-waktu / setiap saat / berkala",
                "level": "N1",
                "example": "質問は随時受け付けています。",
                "example_reading": "しつもんはずいじうけつけています。",
                "example_meaning": "Pertanyaan diterima setiap saat."
            },
            {
                "word": "随分",
                "furigana": "ずいぶん",
                "romaji": "zuibun",
                "meaning": "Sangat / lumayan banyak / luar biasa",
                "level": "N3",
                "example": "日本語が随分上手になりましたね。",
                "example_reading": "にほんごがずいぶんじょうずになりましたね。",
                "example_meaning": "Bahasa Jepangmu sudah sangat pintar ya."
            },
            {
                "word": "追随",
                "furigana": "ついずい",
                "romaji": "tsuizui",
                "meaning": "Mengikuti jejak / meniru di belakang",
                "level": "N1",
                "example": "他社の追随を許さない技術力がある。",
                "example_reading": "たしゃのついずいをゆるさないぎじゅつりょくがある。",
                "example_meaning": "Memiliki keunggulan teknologi yang tidak bisa disaingi perusahaan lain."
            },
            {
                "word": "随筆",
                "furigana": "ずいひつ",
                "romaji": "zuihitsu",
                "meaning": "Esai / tulisan lepas santai",
                "level": "N1",
                "example": "有名な作家の随筆を読むのが好きだ。",
                "example_reading": "ゆうめいなさっかのずいひつをよむのがすきだ。",
                "example_meaning": "Saya suka membaca esai karya penulis terkenal."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "勘",
        "onyomi": "カン",
        "kunyomi": "",
        "meaning": "Intuisi, firasat, perhitungan",
        "jukugo": [
            {
                "word": "勘定",
                "furigana": "かんじょう",
                "romaji": "kanjou",
                "meaning": "Perhitungan / bayar tagihan / rekening",
                "level": "N3",
                "example": "すみません、お勘定をお願いします。",
                "example_reading": "すみません、おかんじょうをおねがいします。",
                "example_meaning": "Permisi, tolong minta bon tagihannya."
            },
            {
                "word": "勘違い",
                "furigana": "かんちがい",
                "romaji": "kanchigai",
                "meaning": "Salah paham / keliru perkiraan",
                "level": "N3",
                "example": "時間を勘違いして早く来てしまった。",
                "example_reading": "じかんをかんちがいしてはやくきてしまった。",
                "example_meaning": "Saya salah mengira jam dan datang terlalu awal."
            },
            {
                "word": "直勘",
                "furigana": "ちょっかん",
                "romaji": "chokkan",
                "meaning": "Intuisi / firasat langsung (直感)",
                "level": "N1",
                "example": "私の直勘が当たった。",
                "example_reading": "わたしのちょっかんがあたった。",
                "example_meaning": "Firasat intuisiku terbukti benar."
            },
            {
                "word": "勘弁",
                "furigana": "かんべん",
                "romaji": "kamben",
                "meaning": "Memaafkan / ampun / mentolerir",
                "level": "N2",
                "example": "冗談はもう勘弁してください。",
                "example_reading": "じょうだんはもうかんべんしてください。",
                "example_meaning": "Tolong sudahi bercandanya, tolong ampunilah."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "佃",
        "onyomi": "デン、テン",
        "kunyomi": "つくだ",
        "meaning": "Sawah garapan, tsukuda",
        "jukugo": [
            {
                "word": "佃煮",
                "furigana": "つくだに",
                "romaji": "tsukudani",
                "meaning": "Tsukudani (lauk rebusan kecap manis dan mirin gurih khas Jepang)",
                "level": "Umum",
                "example": "海苔の佃煮はご飯によく合います。",
                "example_reading": "のりのつくだにはごはんにによくあいます。",
                "example_meaning": "Tsukudani rumput laut sangat cocok dimakan bersama nasi hangat."
            },
            {
                "word": "佃農",
                "furigana": "でんのう",
                "romaji": "dennou",
                "meaning": "Petani penyewa lahan / penggarap sawah",
                "level": "N1",
                "example": "昔の佃農は地主に小作料を払っていた。",
                "example_reading": "むかしのでんのうはじぬしにこさくりょうをはらっていた。",
                "example_meaning": "Petani penggarap zaman dahulu membayar sewa lahan kepada tuan tanah."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "熟",
        "onyomi": "ジュク",
        "kunyomi": "う・れる",
        "meaning": "Matang, terampil, mendalam",
        "jukugo": [
            {
                "word": "熟語",
                "furigana": "じゅくご",
                "romaji": "jukugo",
                "meaning": "Idiom / kata majemuk gabungan kanji",
                "level": "N2",
                "example": "四字熟語を毎日二つ覚えています。",
                "example_reading": "よじじゅくごをまいにちふたつおぼえています。",
                "example_meaning": "Saya menghafal dua idiom 4 karakter (yojijukugo) setiap hari."
            },
            {
                "word": "成熟",
                "furigana": "せいじゅく",
                "romaji": "seijuku",
                "meaning": "Kematangan / kedewasaan",
                "level": "N1",
                "example": "日本は成熟した社会を迎えている。",
                "example_reading": "にほんはせいじゅくしたしゃかいをむかえている。",
                "example_meaning": "Jepang telah memasuki masyarakat yang matang."
            },
            {
                "word": "熟睡",
                "furigana": "じゅくすい",
                "romaji": "jukusui",
                "meaning": "Tidur nyenyak / pulas",
                "level": "N2",
                "example": "昨夜は一度も起きずに熟睡できた。",
                "example_reading": "さくやはいちどもおきずにじゅくすいできた。",
                "example_meaning": "Tadi malam saya tidur pulas tanpa terbangun sekalipun."
            },
            {
                "word": "未熟",
                "furigana": "みじゅく",
                "romaji": "mijuku",
                "meaning": "Belum matang / belum berpengalaman / hijau",
                "level": "N2",
                "example": "まだまだ未熟ですが、精一杯頑張ります。",
                "example_reading": "まだまだみじゅくですが、せいいっぱいがんばります。",
                "example_meaning": "Saya masih belum berpengalaman, tapi saya akan berusaha sekuat tenaga."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "錯",
        "onyomi": "サク",
        "kunyomi": "",
        "meaning": "Bercampur aduk, keliru, silang",
        "jukugo": [
            {
                "word": "錯覚",
                "furigana": "さっかく",
                "romaji": "sakkaku",
                "meaning": "Ilusi optik / salah sangka / keliru persepsi",
                "level": "N1",
                "example": "目の錯覚で二つの線が違う長さに見える。",
                "example_reading": "めのさっかくでふたつのせんがちがうながさにみえる。",
                "example_meaning": "Karena ilusi mata, dua garis tampak berbeda panjangnya."
            },
            {
                "word": "錯誤",
                "furigana": "さくご",
                "romaji": "sakugo",
                "meaning": "Kekeliruan / kesalahan mendasar",
                "level": "N1",
                "example": "時代錯誤な考え方は改めるべきだ。",
                "example_reading": "じだいさくごなかんがえかたはあらためるべきだ。",
                "example_meaning": "Cara berpikir yang ketinggalan zaman (anakronisme) harus diubah."
            },
            {
                "word": "交錯",
                "furigana": "こうさく",
                "romaji": "kousaku",
                "meaning": "Bercampur aduk / bersilangan",
                "level": "N1",
                "example": "期待と不安が交錯する気持ちだ。",
                "example_reading": "きたいとふあんがこうさくするきもちだ。",
                "example_meaning": "Perasaan bercampur aduk antara harapan dan kecemasan."
            },
            {
                "word": "錯乱",
                "furigana": "さくらん",
                "romaji": "sakuran",
                "meaning": "Kekacauan pikiran / linglung / panik bingung",
                "level": "N1",
                "example": "精神錯乱の状態で倒れていた。",
                "example_reading": "せいしんさくらんのじょうたいでたおれていた。",
                "example_meaning": "Dia roboh dalam kondisi linglung kacau pikiran."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "誤",
        "onyomi": "ゴ",
        "kunyomi": "あやま・る",
        "meaning": "Salah, kekeliruan",
        "jukugo": [
            {
                "word": "誤解",
                "furigana": "ごかい",
                "romaji": "gokai",
                "meaning": "Salah paham / kesalahpahaman",
                "level": "N3",
                "example": "私の言葉で誤解を招いてしまった。",
                "example_reading": "わたしのことばでごかいをまねいてしまった。",
                "example_meaning": "Perkataan saya telah menimbulkan salah paham."
            },
            {
                "word": "誤差",
                "furigana": "ごさ",
                "romaji": "gosa",
                "meaning": "Selisih kesalahan / margin of error",
                "level": "N2",
                "example": "測定の誤差をできるだけ小さくする。",
                "example_reading": "そくていのごさをできるだけちいさくする。",
                "example_meaning": "Memperkecil margin kesalahan pengukuran sekecil mungkin."
            },
            {
                "word": "誤診",
                "furigana": "ごしん",
                "romaji": "goshin",
                "meaning": "Salah diagnosis dokter",
                "level": "N1",
                "example": "誤診を防ぐために精密検査を受ける。",
                "example_reading": "ごしんをふせぐためにせいみつけんさをうける。",
                "example_meaning": "Menjalani pemeriksaan menyeluruh untuk mencegah salah diagnosis."
            },
            {
                "word": "誤字",
                "furigana": "ごじ",
                "romaji": "goji",
                "meaning": "Salah tulis / typo / huruf keliru",
                "level": "N2",
                "example": "提出する前に誤字がないか確認する。",
                "example_reading": "ていしゅつするまえにごじがないかかくにんする。",
                "example_meaning": "Memeriksa apakah ada typo sebelum mengumpulkannya."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "極",
        "onyomi": "キョク、ゴク",
        "kunyomi": "きわ・める、きわ・まる",
        "meaning": "Ekstrem, kutub, puncak",
        "jukugo": [
            {
                "word": "極端",
                "furigana": "きょくたん",
                "romaji": "kyokutan",
                "meaning": "Ekstrem / berlebihan",
                "level": "N2",
                "example": "極端なダイエットは体に悪影響を与える。",
                "example_reading": "きょくたんなだいえっとはからだにあくえいきょうをあたえる。",
                "example_meaning": "Diet yang ekstrem memberi dampak buruk bagi tubuh."
            },
            {
                "word": "究極",
                "furigana": "きゅうきょく",
                "romaji": "kyuukyoku",
                "meaning": "Puncak tertinggi / ultimate",
                "level": "N1",
                "example": "究極の選択を迫られた。",
                "example_reading": "きゅうきょくのせんたくをせまられた。",
                "example_meaning": "Dihadapkan pada pilihan yang sangat dilematis/ultimate."
            },
            {
                "word": "北極",
                "furigana": "ほっきょく",
                "romaji": "hokkyoku",
                "meaning": "Kutub Utara",
                "level": "N2",
                "example": "北極の氷が温暖化で溶けている。",
                "example_reading": "ほっきょくのこおりがおんだんかでとけている。",
                "example_meaning": "Es di kutub utara mencair akibat pemanasan global."
            },
            {
                "word": "積極的",
                "furigana": "せっきょくてき",
                "romaji": "sekkyokuteki",
                "meaning": "Positif / proaktif / aktif",
                "level": "N3",
                "example": "会議で積極的に意見を述べた。",
                "example_reading": "かいぎでせっきょくてきにいけんをのべた。",
                "example_meaning": "Menyampaikan pendapat secara aktif dalam rapat."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "範",
        "onyomi": "ハン",
        "kunyomi": "",
        "meaning": "Pola, model, ruang lingkup, teladan",
        "jukugo": [
            {
                "word": "範囲",
                "furigana": "はんい",
                "romaji": "han'i",
                "meaning": "Ruang lingkup / cakupan wilayah / batas jangkauan",
                "level": "N3",
                "example": "試験の範囲がとても広い。",
                "example_reading": "しけんのはんいがとてもひろい。",
                "example_meaning": "Cakupan materi ujian sangat luas."
            },
            {
                "word": "模範",
                "furigana": "もはん",
                "romaji": "mohan",
                "meaning": "Teladan / contoh panutan yang baik",
                "level": "N1",
                "example": "彼はクラスの模範的な生徒だ。",
                "example_reading": "かれはくらすのもはんてきなせいとだ。",
                "example_meaning": "Dia adalah murid teladan di kelas."
            },
            {
                "word": "師範",
                "furigana": "しはん",
                "romaji": "shihan",
                "meaning": "Guru besar / instruktur ahli seni bela diri",
                "level": "N1",
                "example": "空手の師範から直接指導を受けた。",
                "example_reading": "からてのしはんからちょくせつしどうをうけた。",
                "example_meaning": "Mendapat bimbingan langsung dari master guru karate."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "忍",
        "onyomi": "ニン",
        "kunyomi": "しの・ぶ、しの・ばせる",
        "meaning": "Sabar, menyelinap, menahan rasa",
        "jukugo": [
            {
                "word": "忍者",
                "furigana": "にんじゃ",
                "romaji": "ninja",
                "meaning": "Ninja",
                "level": "N3",
                "example": "外国人に忍者の歴史を紹介する。",
                "example_reading": "がいこくじんににんじゃのれきしをしょうかいする。",
                "example_meaning": "Memperkenalkan sejarah ninja kepada orang asing."
            },
            {
                "word": "忍耐",
                "furigana": "にんたい",
                "romaji": "nintai",
                "meaning": "Kesabaran / ketabahan daya tahan",
                "level": "N1",
                "example": "目標を達成するには忍耐が必要だ。",
                "example_reading": "もくひょうをたっせいするにはにんたいがひつようだ。",
                "example_meaning": "Dibutuhkan kesabaran untuk mencapai tujuan."
            },
            {
                "word": "隠忍",
                "furigana": "いんにん",
                "romaji": "innin",
                "meaning": "Menahan diri / bersabar dalam diam",
                "level": "N1",
                "example": "隠忍自重して好機を待つ。",
                "example_reading": "いんにんじちょうしてこうきをまつ。",
                "example_meaning": "Menahan diri dengan sabar sambil menunggu kesempatan baik."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "看",
        "onyomi": "カン",
        "kunyomi": "み・る",
        "meaning": "Melihat, merawat, mengamati",
        "jukugo": [
            {
                "word": "看護",
                "furigana": "かんご",
                "romaji": "kango",
                "meaning": "Perawatan pasien / keperawatan",
                "level": "N3",
                "example": "母が入院中、看護師さんに助けられた。",
                "example_reading": "ははがにゅういんちゅう、かんごしさんにたすけられた。",
                "example_meaning": "Saat ibu dirawat, kami sangat terbantu oleh perawat."
            },
            {
                "word": "看板",
                "furigana": "かんばん",
                "romaji": "kamban",
                "meaning": "Papan nama toko / plang iklan / maskot toko",
                "level": "N3",
                "example": "駅前に大きな看板が立っている。",
                "example_reading": "えきまえにおおきなかんばんがたっている。",
                "example_meaning": "Di depan stasiun berdiri papan plang yang besar."
            },
            {
                "word": "看過",
                "furigana": "かんか",
                "romaji": "kanka",
                "meaning": "Mengabaikan / membiarkan begitu saja / tutup mata",
                "level": "N1",
                "example": "この不正は看過できない問題だ。",
                "example_reading": "このふせいはかんかできないもんだいだ。",
                "example_meaning": "Kecurangan ini masalah yang tidak bisa dibiarkan begitu saja."
            },
            {
                "word": "看破",
                "furigana": "かんぱ",
                "romaji": "kampa",
                "meaning": "Membongkar / melihat tembus rahasia/kebohongan",
                "level": "N1",
                "example": "彼の嘘をすぐに見破り、看破した。",
                "example_reading": "かれのうそをすぐにみやぶり、かんぱした。",
                "example_meaning": "Langsung membongkar dan melihat kebohongan yang dia buat."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "蠅",
        "onyomi": "ヨウ",
        "kunyomi": "はえ",
        "meaning": "Lalat",
        "jukugo": [
            {
                "word": "蠅取",
                "furigana": "はえとり",
                "romaji": "haetori",
                "meaning": "Perangkap lalat / pembasmi lalat",
                "level": "Umum",
                "example": "台所に蠅取り紙をつるした。",
                "example_reading": "だいどころにはえとりがみをつるした。",
                "example_meaning": "Menggantung kertas perangkap lalat di dapur."
            },
            {
                "word": "青蠅",
                "furigana": "あおばえ",
                "romaji": "aobae",
                "meaning": "Lalat hijau / lalat bangkai",
                "level": "Umum",
                "example": "夏になると青蠅が飛んでくる。",
                "example_reading": "なつになるとあおばえがとんでくる。",
                "example_meaning": "Saat musim panas lalat hijau mulai berterbangan."
            },
            {
                "word": "蠅声",
                "furigana": "ようせい",
                "romaji": "yousei",
                "meaning": "Suara dengung riuh berisik seperti lalat",
                "level": "N1",
                "example": "蠅声のごとく群衆がざわめいていた。",
                "example_reading": "ようせいのごとくぐんしゅうがざわめいていた。",
                "example_meaning": "Kerumunan orang berdengung riuh seperti suara sekawanan lalat."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "葵",
        "onyomi": "キ",
        "kunyomi": "あおい",
        "meaning": "Bunga aoi (mallow/hollyhock)",
        "jukugo": [
            {
                "word": "向日葵",
                "furigana": "ひまわり",
                "romaji": "himawari",
                "meaning": "Bunga matahari",
                "level": "N2",
                "example": "夏に庭で向日葵が一斉に咲いた。",
                "example_reading": "なつににわでひまわりがいっせいにさいた。",
                "example_meaning": "Di musim panas, bunga matahari bermekaran serentak di taman."
            },
            {
                "word": "葵祭",
                "furigana": "あおいまつり",
                "romaji": "aoimatsuri",
                "meaning": "Festival Aoi Matsuri (Festival kuno terkenal di Kyoto)",
                "level": "Umum",
                "example": "五月に京都で葵祭が行われる。",
                "example_reading": "ごがつにきょうとであおいまつりがおこなわれる。",
                "example_meaning": "Pada bulan Mei, festival Aoi Matsuri diselenggarakan di Kyoto."
            },
            {
                "word": "山葵",
                "furigana": "わさび",
                "romaji": "wasabi",
                "meaning": "Wasabi (sambal pedas hijau khas Jepang)",
                "level": "N3",
                "example": "寿司に山葵を少し多めにつける。",
                "example_reading": "すしにわさびをすこしおおめにつける。",
                "example_meaning": "Menambahkan sedikit lebih banyak wasabi pada sushi."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "倫",
        "onyomi": "リン",
        "kunyomi": "",
        "meaning": "Etika, moral, tatanan moral",
        "jukugo": [
            {
                "word": "倫理",
                "furigana": "りんり",
                "romaji": "rinri",
                "meaning": "Etika / moralitas",
                "level": "N1",
                "example": "科学者としての職業倫理を守る。",
                "example_reading": "かがくしゃとしてのしょくぎょうりんりをまもる。",
                "example_meaning": "Menjunjung etika profesi sebagai seorang ilmuwan."
            },
            {
                "word": "不倫",
                "furigana": "ふりん",
                "romaji": "furin",
                "meaning": "Perselingkuhan / perzinaan / hubungan gelap",
                "level": "N2",
                "example": "有名人の不倫報道が話題になった。",
                "example_reading": "ゆうめいじんのふりんほうどうがわだいになった。",
                "example_meaning": "Berita perselingkuhan selebritas menjadi perbincangan hangat."
            },
            {
                "word": "倫理観",
                "furigana": "りんりかん",
                "romaji": "rinrikan",
                "meaning": "Pandangan nilai etika / pedoman moral",
                "level": "N1",
                "example": "高い倫理観を持って行動する。",
                "example_reading": "たかいりんりかんをもってこうどうする。",
                "example_meaning": "Bertindak dengan menjunjung tinggi nilai-nilai moralitas."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "敦",
        "onyomi": "トン",
        "kunyomi": "",
        "meaning": "Tulus, ramah, hangat hati",
        "jukugo": [
            {
                "word": "敦厚",
                "furigana": "とんこう",
                "romaji": "tonkou",
                "meaning": "Tulus hati / ramah berhati mulia",
                "level": "N1",
                "example": "先生の人柄は温和で敦厚である。",
                "example_reading": "せんせいのひとがらはおんわでとんこうである。",
                "example_meaning": "Kepribadian guru itu lemah lembut dan berhati tulus mulia."
            },
            {
                "word": "敦賀",
                "furigana": "つるが",
                "romaji": "tsuruga",
                "meaning": "Tsuruga (kota pelabuhan & stasiun Shinkansen di Prefektur Fukui)",
                "level": "Umum",
                "example": "北陸新幹線が敦賀まで延伸された。",
                "example_reading": "ほくりくしんかんせんがつるがまでえんしんされた。",
                "example_meaning": "Jalur Hokuriku Shinkansen diperpanjang hingga stasiun Tsuruga."
            },
            {
                "word": "敦睦",
                "furigana": "とんぼく",
                "romaji": "tomboku",
                "meaning": "Keakraban yang tulus / persahabatan harmonis",
                "level": "N1",
                "example": "隣国との敦睦を深める。",
                "example_reading": "りんごくとのとんぼくをふかめる。",
                "example_meaning": "Memperdalam keharmonisan dan persahabatan dengan negara tetangga."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "情",
        "onyomi": "ジョウ、セイ",
        "kunyomi": "なさ・け",
        "meaning": "Informasi, perasaan, emosi, kasih sayang",
        "jukugo": [
            {
                "word": "情報",
                "furigana": "じょうほう",
                "romaji": "jouhou",
                "meaning": "Informasi / data kabar",
                "level": "N3",
                "example": "インターネットで最新の情報を調べる。",
                "example_reading": "いんたーねっとでさいしんのじょうほうをしらべる。",
                "example_meaning": "Mencari informasi terbaru di internet."
            },
            {
                "word": "感情",
                "furigana": "かんじょう",
                "romaji": "kanjou",
                "meaning": "Emosi / perasaan batin",
                "level": "N3",
                "example": "感情をコントロールするのは大切だ。",
                "example_reading": "かんじょうをこんとろーるするのはたいせつだ。",
                "example_meaning": "Mengendalikan emosi itu sangat penting."
            },
            {
                "word": "表情",
                "furigana": "ひょうじょう",
                "romaji": "hyoujou",
                "meaning": "Ekspresi raut muka",
                "level": "N3",
                "example": "彼の表情から不安が伝わってきた。",
                "example_reading": "かれのひょうじょうからふあんがつたわってきた。",
                "example_meaning": "Kecemasan terasa jelas dari ekspresi wajahnya."
            },
            {
                "word": "友情",
                "furigana": "ゆうじょう",
                "romaji": "yuujou",
                "meaning": "Persahabatan",
                "level": "N3",
                "example": "長年の友情を大切にしたい。",
                "example_reading": "ながねんのゆうじょうをたいせつにしたい。",
                "example_meaning": "Saya ingin menjaga persahabatan yang telah terjalin bertahun-tahun."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "息",
        "onyomi": "ソク",
        "kunyomi": "いき",
        "meaning": "Napas, anak laki-laki, berhenti",
        "jukugo": [
            {
                "word": "息",
                "furigana": "いき",
                "romaji": "iki",
                "meaning": "Napas",
                "level": "N4",
                "example": "階段を上って息が切れた。",
                "example_reading": "かいだんをのぼっていきがきれた。",
                "example_meaning": "Napas saya terengah-engah setelah menaiki tangga."
            },
            {
                "word": "息子",
                "furigana": "むすこ",
                "romaji": "musuko",
                "meaning": "Anak laki-laki",
                "level": "N4",
                "example": "息子は大学で物理を専攻している。",
                "example_reading": "むすこはだいがくでぶつりをせんこうしている。",
                "example_meaning": "Anak laki-laki saya mengambil jurusan fisika di universitas."
            },
            {
                "word": "休息",
                "furigana": "きゅうそく",
                "romaji": "kyuusoku",
                "meaning": "Istirahat santai / jeda rehat",
                "level": "N2",
                "example": "適度に休息を取りながら勉強しよう。",
                "example_reading": "てきどにきゅうそくをとりながらべんきょうしよう。",
                "example_meaning": "Mari belajar sambil mengambil istirahat secukupnya."
            },
            {
                "word": "利息",
                "furigana": "りそく",
                "romaji": "risoku",
                "meaning": "Bunga uang / bunga pinjaman/tabungan",
                "level": "N2",
                "example": "銀行預金に利息がついた。",
                "example_reading": "ぎんこうよきんにりそくがついた。",
                "example_meaning": "Tabungan di bank mendapatkan bunga."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "影",
        "onyomi": "エイ",
        "kunyomi": "かげ",
        "meaning": "Bayangan, bayang-bayang, foto",
        "jukugo": [
            {
                "word": "影響",
                "furigana": "えいきょう",
                "romaji": "eikyou",
                "meaning": "Pengaruh / efek dampak",
                "level": "N3",
                "example": "親の行動は子供に大きな影響を与える。",
                "example_reading": "おやのこうどうはこどもにおおきなえいきょうをあたえる。",
                "example_meaning": "Tindakan orang tua memberi pengaruh besar kepada anak."
            },
            {
                "word": "撮影",
                "furigana": "さつえい",
                "romaji": "satsuei",
                "meaning": "Pemotretan / perekaman video / syuting",
                "level": "N2",
                "example": "美術館内での撮影は禁止です。",
                "example_reading": "びじゅつかんないでのさつえいはきんしです。",
                "example_meaning": "Pemotretan di dalam gedung museum dilarang."
            },
            {
                "word": "幻影",
                "furigana": "げんえい",
                "romaji": "gen'ei",
                "meaning": "Bayangan ilusi / fatamorgana",
                "level": "N1",
                "example": "砂漠で幻影を見たような気がした。",
                "example_reading": "さばくでげんえいをみたようなきがした。",
                "example_meaning": "Terasa seolah melihat bayangan ilusi di padang pasir."
            },
            {
                "word": "面影",
                "furigana": "おもかげ",
                "romaji": "omokage",
                "meaning": "Guratan wajah kenangan / bayang raut masa lalu",
                "level": "N1",
                "example": "彼女には昔の面影が残っている。",
                "example_reading": "かのじょにはむかしのおもかげがのこっている。",
                "example_meaning": "Raut wajah masa lalunya masih tersisa pada dirinya."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "響",
        "onyomi": "キョウ",
        "kunyomi": "ひび・く",
        "meaning": "Gema, suara bergaung, getaran suara",
        "jukugo": [
            {
                "word": "反響",
                "furigana": "はんきょう",
                "romaji": "hankyou",
                "meaning": "Reaksi tanggapan / gema gaung",
                "level": "N1",
                "example": "新商品は大きな反響を呼んだ。",
                "example_reading": "しんしょうひんはおおきなはんきょうをよんだ。",
                "example_meaning": "Produk baru tersebut menuai tanggapan yang luar biasa."
            },
            {
                "word": "音響",
                "furigana": "おんきょう",
                "romaji": "onkyou",
                "meaning": "Akustik / efek tata suara",
                "level": "N1",
                "example": "このホールは音響設備が素晴らしい。",
                "example_reading": "このほーるはおんきょうせつびがすばらしい。",
                "example_meaning": "Gedung ini memiliki fasilitas akustik yang luar biasa."
            },
            {
                "word": "交響曲",
                "furigana": "こうきょうきょく",
                "romaji": "koukyoukyoku",
                "meaning": "Simfoni (karya musik orkestra)",
                "level": "N1",
                "example": "ベートーヴェンの交響曲第九番を聴く。",
                "example_reading": "べーとーべんのこうきょうきょくだいきゅうばんをきく。",
                "example_meaning": "Mendengarkan simfoni no. 9 karya Beethoven."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "愉",
        "onyomi": "ユ",
        "kunyomi": "たの・しい",
        "meaning": "Senang, menyenangkan, riang",
        "jukugo": [
            {
                "word": "愉快",
                "furigana": "ゆかい",
                "romaji": "yukai",
                "meaning": "Menyenangkan / lucu menghibur / ceria",
                "level": "N2",
                "example": "昨日のパーティーは愉快な仲間と過ごせた。",
                "example_reading": "きのうのぱーてぃーはゆかいななかまとすごせた。",
                "example_meaning": "Pesta kemarin dilewati bersama teman-teman yang menyenangkan."
            },
            {
                "word": "愉悦",
                "furigana": "ゆえつ",
                "romaji": "yuetsu",
                "meaning": "Sukacita mendalam / kegembiraan hati",
                "level": "N1",
                "example": "読書の愉悦に浸る時間は至福だ。",
                "example_reading": "どくしょのゆえつにひたるじかんはしふくだ。",
                "example_meaning": "Tenggelam dalam sukacita membaca buku adalah waktu yang penuh berkah."
            },
            {
                "word": "愉楽",
                "furigana": "ゆらく",
                "romaji": "yuraku",
                "meaning": "Kenikmatan bersenang-senang / hiburan ria",
                "level": "N1",
                "example": "温泉旅行で心身の愉楽を味わう。",
                "example_reading": "おんせんりょこうでしんしんのゆらくをあじわう。",
                "example_meaning": "Merasakan kenikmatan jiwa dan raga dalam wisata pemandian air panas."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "快",
        "onyomi": "カイ",
        "kunyomi": "こころよ・い",
        "meaning": "Nyaman, menyenangkan, pulih",
        "jukugo": [
            {
                "word": "快適",
                "furigana": "かいてき",
                "romaji": "kaiteki",
                "meaning": "Nyaman / enak dihuni atau dipakai",
                "level": "N3",
                "example": "ホテルの部屋は広くて快適だった。",
                "example_reading": "ほてるのへやはひろくてかいてきだった。",
                "example_meaning": "Kamar hotelnya luas dan sangat nyaman."
            },
            {
                "word": "快晴",
                "furigana": "かいせい",
                "romaji": "kaisei",
                "meaning": "Cuaca cerah benderang tanpa awan",
                "level": "N3",
                "example": "今日は雲一つない快晴だ。",
                "example_reading": "きょうはくもひとつないかいせいだ。",
                "example_meaning": "Hari ini cuaca cerah tanpa satu awan pun."
            },
            {
                "word": "爽快",
                "furigana": "そうかい",
                "romaji": "soukai",
                "meaning": "Segar bugar / menyegarkan",
                "level": "N1",
                "example": "朝の運動は気分が爽快になる。",
                "example_reading": "あさのうんどうはきぶんがそうかいになる。",
                "example_meaning": "Olahraga pagi membuat perasaan terasa sangat segar."
            },
            {
                "word": "快復",
                "furigana": "かいふく",
                "romaji": "kaifuku",
                "meaning": "Pemulihan kesehatan / lekas sembuh",
                "level": "N2",
                "example": "一日も早いご快復をお祈り申し上げます。",
                "example_reading": "いちにちもはやいごかいふくをおいのりもうしあげます。",
                "example_meaning": "Saya mendoakan agar Anda lekas pulih secepatnya."
            }
        ]
    },
    {
        "week": 1,
        "kanji": "素",
        "onyomi": "ソ、ス",
        "kunyomi": "もと",
        "meaning": "Unsur, polos, asli, sederhana",
        "jukugo": [
            {
                "word": "素直",
                "furigana": "すなお",
                "romaji": "sunao",
                "meaning": "Penurut / jujur apa adanya / terbuka hati",
                "level": "N3",
                "example": "自分の非を素直に認めて謝った。",
                "example_reading": "じぶんのひをすなおにみとめてあやまった。",
                "example_meaning": "Mengakui kesalahan diri secara jujur dan meminta maaf."
            },
            {
                "word": "素敵",
                "furigana": "すてき",
                "romaji": "suteki",
                "meaning": "Bagus sekali / indah mempesona",
                "level": "N4",
                "example": "とても素敵な服を着ていますね。",
                "example_reading": "とてもすてきなふくをきていますね。",
                "example_meaning": "Kamu memakai baju yang sangat bagus ya."
            },
            {
                "word": "要素",
                "furigana": "ようそ",
                "romaji": "youso",
                "meaning": "Unsur / elemen faktor penting",
                "level": "N2",
                "example": "成功のための重要な要素を分析する。",
                "example_reading": "せいこうのためのじゅうようなようそをぶんせきする。",
                "example_meaning": "Menganalisis elemen-elemen penting untuk meraih kesuksesan."
            },
            {
                "word": "素朴",
                "furigana": "そぼく",
                "romaji": "soboku",
                "meaning": "Sederhana / polos bersahaja tanpa dibuat-buat",
                "level": "N1",
                "example": "田舎の素朴な暮らしに憧れる。",
                "example_reading": "いなかのそぼくなくらしにあこがれる。",
                "example_meaning": "Saya mendambakan kehidupan sederhana bersahaja di pedesaan."
            }
        ]
    }
]

print(f"Minggu 1 loaded: {len(raw_data)} kanji.")
