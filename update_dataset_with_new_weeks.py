# -*- coding: utf-8 -*-
"""
Script to compile all weeks: Weeks 1-6 AND Weeks 9-14 into data.js.
Ensures every kanji has between 2 and 4 high-frequency jukugo.
"""
import json
import sys

# Load existing generate_full_data.py content or define complete dataset
from generate_full_data import DATA as EXISTING_DATA

NEW_DATA = []

def add_kanji(week, kanji, onyomi, kunyomi, meaning, jukugo_list, note=None):
    assert 2 <= len(jukugo_list) <= 4, f"Kanji {kanji} must have between 2 and 4 jukugo, got {len(jukugo_list)}"
    item = {
        "week": week,
        "kanji": kanji,
        "onyomi": onyomi,
        "kunyomi": kunyomi,
        "meaning": meaning,
        "jukugo": jukugo_list
    }
    if note:
        item["note"] = note
    NEW_DATA.append(item)

# ==========================================
# MINGGU 9
# 唱、翌、創、添、純、絞、養、砲、芯、巻、劇、秀、脚、装、華、積、噺、継、露、豊、就、防、詐、欺、順、躍、漠、梅
# (duplicates removed: 劇, 養)
# ==========================================
add_kanji(9, "唱", "ショウ", "とな・える", "Menyanyi, mendaraskan, menyerukan", [
    {"word": "合唱", "furigana": "がっしょう", "romaji": "gasshou", "meaning": "Paduan suara / bernyanyi bersama", "level": "N2", "example": "クラス全員で合唱コンクールに出場する。", "example_reading": "くらすぜんいんでがっしょうこんくーるにしゅつじょうする。", "example_meaning": "Seluruh kelas ikut serta dalam lomba paduan suara."},
    {"word": "提唱", "furigana": "ていしょう", "romaji": "teishou", "meaning": "Advokasi / mengusulkan gagasan baru", "level": "N1", "example": "新しい環境保護の理念を提唱した。", "example_reading": "あたらしいかんきょうほごのりねんをていしょうした。", "example_meaning": "Mengadvokasikan gagasan filosofi perlindungan lingkungan baru."},
    {"word": "唱道", "furigana": "しょうどう", "romaji": "shoudou", "meaning": "Menyerukan doktrin / mempropagandakan", "level": "N1", "example": "平和主義を唱道する運動を展開する。", "example_reading": "へいわしゅぎをしょうどうするうんどうをてんかいする。", "example_meaning": "Mengembangkan gerakan yang menyerukan paham perdamaian."}
])

add_kanji(9, "翌", "ヨク", "", "Berikutnya, esok hari/tahun", [
    {"word": "翌日", "furigana": "よくじつ", "romaji": "yokujitsu", "meaning": "Keesokan harinya / hari berikutnya", "level": "N3", "example": "パーティーの翌日は家でゆっくり休んだ。", "example_reading": "ぱーてぃーのよくじつはいえでゆっくりやすんだ。", "example_meaning": "Keesokan harinya setelah pesta, saya beristirahat santai di rumah."},
    {"word": "翌朝", "furigana": "よくあさ", "romaji": "yokuasa", "meaning": "Keesokan paginya", "level": "N2", "example": "翌朝早く起きて散歩に出かけた。", "example_reading": "よくあさはやくおきてさんぽにでかけた。", "example_meaning": "Keesokan paginya bangun awal dan pergi jalan-jalan."},
    {"word": "翌年", "furigana": "よくねん", "romaji": "yokunen", "meaning": "Tahun berikutnya", "level": "N2", "example": "卒業した翌年に留学を果たした。", "example_reading": "そつぎょうしたよくねんにりゅうがくをはたした。", "example_meaning": "Tahun berikutnya setelah lulus, berhasil mewujudkan studi ke luar negeri."}
])

add_kanji(9, "創", "ソウ", "つく・る", "Menciptakan kreasi permulaan", [
    {"word": "創造", "furigana": "そうぞう", "romaji": "souzou", "meaning": "Penciptaan kreasi ide baru", "level": "N2", "example": "AIとともに新しい芸術を創造する。", "example_reading": "えーあいとともにあたらしいげいじゅつをそうぞうする。", "example_meaning": "Menciptakan seni baru bersama kecerdasan buatan (AI)."},
    {"word": "創立", "furigana": "そうりつ", "romaji": "souritsu", "meaning": "Pendirian lembaga atau sekolah", "level": "N2", "example": "今年で会社創立五十周年を迎える。", "example_reading": "ことしでかいしゃそうりつごじゅっしゅうねんをむかえる。", "example_meaning": "Tahun ini menyambut peringatan 50 tahun pendirian perusahaan."},
    {"word": "創作", "furigana": "そうさく", "romaji": "sousaku", "meaning": "Karya cipta / kreasi sastra seni", "level": "N2", "example": "オリジナルの創作料理を振る舞った。", "example_reading": "おりじなるのそうさくりょうりをふるまった。", "example_meaning": "Menyajikan hidangan kreasi orisinal buatan sendiri."}
])

add_kanji(9, "添", "テン", "そ・える、そ・う", "Melampirkan, menambahkan, menyertakan", [
    {"word": "添付", "furigana": "てんぷ", "romaji": "tempu", "meaning": "Lampiran berkas file email", "level": "N2", "example": "メールに履歴書のファイルを添付した。", "example_reading": "めーるにりれきしょのふぁいるをてんぷした。", "example_meaning": "Melampirkan berkas CV pada surat elektronik."},
    {"word": "添加", "furigana": "てんか", "romaji": "tenka", "meaning": "Penambahan zat aditif kimia", "level": "N1", "example": "食品添加物を含まない安全な食材を選ぶ。", "example_reading": "しょくひんてんかぶつをふくまないあんぜんなしょくざいをえらぶ。", "example_meaning": "Memilih bahan pangan aman yang bebas dari zat aditif makanan."},
    {"word": "添削", "furigana": "てんさく", "romaji": "tensaku", "meaning": "Koreksi penyuntingan tulisan naskah", "level": "N1", "example": "先生に作文を丁寧に添削してもらった。", "example_reading": "せんせいにさくぶんをていねいにてんさくしてもらった。", "example_meaning": "Karangan saya dikoreksi dan disunting dengan teliti oleh guru."}
])

add_kanji(9, "純", "ジュン", "", "Murni, polos, tulus", [
    {"word": "純粋", "furigana": "じゅんすい", "romaji": "junsui", "meaning": "Murni / suci tanpa campuran", "level": "N2", "example": "子供の純粋な心に感動した。", "example_reading": "こどものじゅんすいなこころにかんどうした。", "example_meaning": "Terharu oleh hati anak-anak yang begitu murni tulus."},
    {"word": "純情", "furigana": "じゅんじょう", "romaji": "junjou", "meaning": "Polos lugu berhati bersih", "level": "N1", "example": "純情な青年の恋を描いた映画だ。", "example_reading": "じゅんじょうなせいねんのこいをえがいたえいがだ。", "example_meaning": "Film yang menggambarkan kisah cinta pemuda yang polos lugu."},
    {"word": "単純", "furigana": "たんじゅん", "romaji": "tanjun", "meaning": "Sederhana simpel mudah dipahami", "level": "N3", "example": "この機械の構造はとても単純だ。", "example_reading": "このきかいのこうぞうはとてもたんじゅんだ。", "example_meaning": "Struktur mesin ini sangat sederhana dan mudah dimengerti."}
])

add_kanji(9, "絞", "コウ", "しぼ・る", "Memeras, mencekik, menyempitkan", [
    {"word": "絞殺", "furigana": "こうさつ", "romaji": "kousatsu", "meaning": "Pembunuhan dengan cara dicekik", "level": "N1", "example": "警察が絞殺事件の現場を調査した。", "example_reading": "けいさつがこうさつじけんのげんばをちょうさした。", "example_meaning": "Polisi menyelidiki tempat kejadian perkara pembunuhan cekik."},
    {"word": "絞首", "furigana": "こうしゅ", "romaji": "koushu", "meaning": "Hukuman gantung leher", "level": "N1", "example": "重罪人に対して絞首刑が言い渡された。", "example_reading": "じゅうざいにんにたいしてこうしゅけいがいいわたされた。", "example_meaning": "Hukuman gantung dijatuhkan kepada terdakwa pelaku kejahatan berat."},
    {"word": "絞り染め", "furigana": "しぼりぞめ", "romaji": "shiborizome", "meaning": "Kain celup ikat khas Jepang (shibori)", "level": "Umum", "example": "伝統工芸の絞り染めの布を買った。", "example_reading": "でんとうこうげいのしぼりぞめのぬのをおかった。", "example_meaning": "Membeli kain celup ikat shibori hasil kerajinan tradisional."}
])

add_kanji(9, "養", "ヨウ", "やしな・う", "Merawat, menutrisi, membudidayakan", [
    {"word": "栄養", "furigana": "えいよう", "romaji": "eiyou", "meaning": "Gizi nutrisi makanan", "level": "N3", "example": "健康のために栄養バランスの良い食事をとる。", "example_reading": "けんこうのためにえいようばらんすのよいしょくじをとる。", "example_meaning": "Menjaga pola makan bergizi seimbang demi kesehatan."},
    {"word": "養殖", "furigana": "ようしょく", "romaji": "youshoku", "meaning": "Budidaya ternak perikanan akuakultur", "level": "N1", "example": "湾内で真珠の養殖が行われている。", "example_reading": "わんないでしんじゅのようしょくがおこなわれている。", "example_meaning": "Budidaya kerang mutiara dilakukan di dalam teluk."},
    {"word": "養成", "furigana": "ようせい", "romaji": "yousei", "meaning": "Pembinaan pelatihan mendidik bibit ahli", "level": "N1", "example": "プロの通訳者を養成する専門学校だ。", "example_reading": "ぷろのつうやくしゃをようせいするせんもんがっこうだ。", "example_meaning": "Sekolah kejuruan yang membina dan melatih penerjemah profesional."}
])

add_kanji(9, "砲", "ホウ", "", "Meriam, senapan, tembakan artileri", [
    {"word": "大砲", "furigana": "たいほう", "romaji": "taihou", "meaning": "Meriam besar artileri", "level": "N2", "example": "古城の城壁に大砲が据えられている。", "example_reading": "こじょうのじょうへきにたいほうがすえられている。", "example_meaning": "Meriam besar terpasang di atas dinding benteng istana kuno."},
    {"word": "鉄砲", "furigana": "てっぽう", "romaji": "teppou", "meaning": "Senapan senjata api", "level": "N2", "example": "戦国時代に種子島へ鉄砲が伝来した。", "example_reading": "せんごくじだいにたねがしまへてっぽうがでんらいした。", "example_meaning": "Senjata api pertama kali masuk ke pulau Tanegashima di zaman Sengoku."},
    {"word": "砲撃", "furigana": "ほうげき", "romaji": "hougeki", "meaning": "Serangan tembakan meriam artileri", "level": "N1", "example": "激しい砲撃で要塞が破壊された。", "example_reading": "はげしいほうげきでようさいがはかいされた。", "example_meaning": "Benteng pertahanan hancur oleh rentetan tembakan meriam yang sengit."}
])

add_kanji(9, "芯", "シン", "", "Sumbu, isi pensil, inti tengah", [
    {"word": "替芯", "furigana": "かえしん", "romaji": "kaeshin", "meaning": "Isi ulang tinta pulpen / isi pensil mekanik", "level": "Umum", "example": "シャープペンシルの替芯を文房具屋で買った。", "example_reading": "しゃーぷぺんしるのかえしんをぶんぼうぐやでかった。", "example_meaning": "Membeli isi ulang pensil mekanik di toko alat tulis."},
    {"word": "芯地", "furigana": "しんじ", "romaji": "shinji", "meaning": "Kain pelapis dalam kerah baju (interlining)", "level": "N1", "example": "襟にしっかりとした芯地を入れる。", "example_reading": "えりにしっかりとしたしんじをいれる。", "example_meaning": "Memasukkan kain pelapis yang kokoh pada kerah baju."},
    {"word": "芯棒", "furigana": "しんぼう", "romaji": "shimbou", "meaning": "Poros inti tongkat as tengah", "level": "N1", "example": "車輪の芯棒に油をさして回転を滑らかにする。", "example_reading": "しゃりんのしんぼうにあぶらをさしてかいてんをなめらかにする。", "example_meaning": "Melumasi poros roda dengan oli agar putarannya lancar."}
])

add_kanji(9, "巻", "カン", "ま・く、ま・き", "Jilid volume, menggulung", [
    {"word": "全巻", "furigana": "ぜんかん", "romaji": "zenkan", "meaning": "Seluruh jilid lengkap satu set", "level": "N2", "example": "大好きなマンガの全巻を一気に読んだ。", "example_reading": "だいすきなまんがのぜんかんをいっきによんだ。", "example_meaning": "Membaca tuntas seluruh jilid komik favorit sekaligus."},
    {"word": "巻末", "furigana": "かんまつ", "romaji": "kammatsu", "meaning": "Bagian akhir jilid lembar penutup buku", "level": "N1", "example": "巻末の用語解説を参照してください。", "example_reading": "かんまつのようごかいせつをさんしょうしてください。", "example_meaning": "Silakan merujuk ke penjelasan glosarium di bagian akhir buku."},
    {"word": "圧巻", "furigana": "あっかん", "romaji": "akkan", "meaning": "Mahakarya adegan terbaik puncak pertunjukan", "level": "N1", "example": "クライマックスの戦闘シーンはまさに圧巻だった。", "example_reading": "くらいまっくすのせんとうしーんはまさにあっかんだった。", "example_meaning": "Adegan pertempuran di puncak klimaks benar-benar mahakarya yang memukau."}
])

add_kanji(9, "劇", "ゲキ", "", "Drama teater sandiwara drastis", [
    {"word": "劇場", "furigana": "げきじょう", "romaji": "gekijou", "meaning": "Gedung teater pertunjukan", "level": "N3", "example": "有名な劇場でミュージカルを鑑賞した。", "example_reading": "ゆうめいなげきじょうでみゅーじかるをかんしょうした。", "example_meaning": "Menikmati pertunjukan teater musikal di gedung teater ternama."},
    {"word": "演劇", "furigana": "えんげき", "romaji": "engeki", "meaning": "Seni drama pementasan teater", "level": "N2", "example": "大学の演劇サークルで主役を演じた。", "example_reading": "だいがくのえんげきさーくるでしゅやくをえんじた。", "example_meaning": "Memerankan tokoh utama di klub seni teater universitas."},
    {"word": "劇的", "furigana": "げきてき", "romaji": "gekiteki", "meaning": "Dramatis luar biasa menggugah", "level": "N1", "example": "試合終了直前の劇的な逆転ゴールに沸いた。", "example_reading": "しあいしゅうりょうちょくぜんのげきてきなぎゃくてんごーるにわいた。", "example_meaning": "Bersorak atas gol pembalik keadaan yang dramatis tepat sebelum laga usai."}
])

add_kanji(9, "秀", "シュウ", "ひい・でる", "Unggul terkemuka istimewa", [
    {"word": "優秀", "furigana": "ゆうしゅう", "romaji": "yuushuu", "meaning": "Unggul berprestasi istimewa pintar", "level": "N2", "example": "彼は優秀な成績で大学を卒業した。", "example_reading": "かれはゆうしゅうなせいせきでだいがくをそつぎょうした。", "example_meaning": "Dia lulus dari universitas dengan prestasi yang sangat unggul."},
    {"word": "秀才", "furigana": "しゅうさい", "romaji": "shuusai", "meaning": "Anak berbakat orang jenius cerdas", "level": "N1", "example": "数学の秀才として全国に名を知られている。", "example_reading": "すうがくのしゅうさいとしてぜんこくにめい আল্লাহをينةられている。", "example_meaning": "Dikenal di seluruh pelosok negeri sebagai anak jenius matematika."},
    {"word": "秀逸", "furigana": "しゅういつ", "romaji": "shuuitsu", "meaning": "Luar biasa brilian cemerlang menonjol", "level": "N1", "example": "この広告のキャッチコピーは実に秀逸だ。", "example_reading": "このこうこくのきゃっちこぴーはじつにしゅういつだ。", "example_meaning": "Kalimat slogan iklan ini benar-benar sangat brilian dan cemerlang."}
])

add_kanji(9, "脚", "キャク、キャ", "あし", "Kaki tumpuan skenario", [
    {"word": "脚本", "furigana": "きゃくほん", "romaji": "kyakuhon", "meaning": "Naskah skenario drama skrip", "level": "N2", "example": "映画の脚本家を目指して勉強している。", "example_reading": "えいがのきゃくほんかをござしてべんきょうしている。", "example_meaning": "Belajar tekun untuk meraih cita-cita menjadi penulis skenario film."},
    {"word": "脚色", "furigana": "きゃくしょく", "romaji": "kyakushoku", "meaning": "Dramatisasi adaptasi cerita fiksi", "level": "N1", "example": "歴史的事実を脚色して物語を面白くした。", "example_reading": "れきしてきじじつをきゃくしょくしてものがたりをおもしろくした。", "example_meaning": "Mendramatisasi fakta sejarah agar alur ceritanya semakin menarik."},
    {"word": "三脚", "furigana": "さんきゃく", "romaji": "sankyaku", "meaning": "Tripod kaki tiga dudukan kamera", "level": "N2", "example": "夜景をきれいに撮るために三脚を使う。", "example_reading": "やけいをきれいににるためにさんきゃくをつかう。", "example_meaning": "Menggunakan tripod agar bisa memotret pemandangan malam dengan jernih."}
])

add_kanji(9, "装", "ソウ、ショウ", "よそお・う", "Pakaian perlengkapan dekorasi rakit", [
    {"word": "装置", "furigana": "そうち", "romaji": "souchi", "meaning": "Peralatan perangkat instrumen sistem", "level": "N2", "example": "安全装置が作動して事故を防いだ。", "example_reading": "あんぜんそうちがさどうしてじこをふせいだ。", "example_meaning": "Perangkat keselamatan berfungsi aktif dan berhasil mencegah kecelakaan."},
    {"word": "衣装", "furigana": "いしょう", "romaji": "ishou", "meaning": "Kostum busana panggung gaun", "level": "N2", "example": "演劇の舞台衣装を手作りで制作した。", "example_reading": "えんげきのぶたいいしょうをてづくりでせいさくした。", "example_meaning": "Membuat kostum panggung pertunjukan drama secara swakarya."},
    {"word": "装飾", "furigana": "そうしょく", "romaji": "soushoku", "meaning": "Dekorasi ornamen perhiasan mempercantik", "level": "N1", "example": "クリスマスの装飾で街が華やかに彩られた。", "example_reading": "くりすますのそうしょくでまちがはなやかにいろどられた。", "example_meaning": "Kota dihiasi semarak memesona dengan berbagai dekorasi Natal."}
])

add_kanji(9, "華", "カ、ケ", "はな", "Bunga mekar, megah gemerlap mewah", [
    {"word": "華麗", "furigana": "かれい", "romaji": "karei", "meaning": "Megah mewah memesona berkilau anggun", "level": "N1", "example": "華麗なダンスで観客を魅了した。", "example_reading": "かれいなだんすでかんきゃくをみりょうした。", "example_meaning": "Memikat hati para penonton dengan tarian yang begitu megah dan anggun."},
    {"word": "繁華", "furigana": "はんか", "romaji": "hanka", "meaning": "Ramai gemerlap pusat keramaian kota", "level": "N1", "example": "駅周辺の繁華街は夜遅くまで賑わっている。", "example_reading": "えきしゅうへんのはんかがいはよるおそくまでにぎわっている。", "example_meaning": "Pusat keramaian gemerlap di sekitar stasiun ramai hingga larut malam."},
    {"word": "華美", "furigana": "かび", "romaji": "kabi", "meaning": "Kemewahan berlebihan mencolok", "level": "N1", "example": "華美な服装を避けて質素な身なりを心がける。", "example_reading": "かびなふくそうをさけてしっそなみなりをこころがける。", "example_meaning": "Menghindari busana yang terlalu mewah mencolok dan berpenampilan sederhana."}
])

add_kanji(9, "積", "セキ", "つ・む、つ・もる", "Menumpuk mengumpulkan akumulasi", [
    {"word": "積極的", "furigana": "せっきょくてき", "romaji": "sekkyokuteki", "meaning": "Proaktif giat positif bersemangat", "level": "N3", "example": "会議で自分の意見を積極的に発言する。", "example_reading": "かいぎでじぶんのいけんをせっきょくてきにはつげんする。", "example_meaning": "Menyampaikan pendapat secara proaktif di dalam rapat."},
    {"word": "蓄積", "furigana": "ちくせき", "romaji": "chikuseki", "meaning": "Akumulasi penimbunan bertahap", "level": "N1", "example": "日々の勉強の蓄積が合格につながる。", "example_reading": "ひびのべんきょうのちくせきがごうかくにつながる。", "example_meaning": "Akumulasi belajar harian akan mengantarkan pada kelulusan."},
    {"word": "面積", "furigana": "めんせき", "romaji": "menseki", "meaning": "Luas area bidang wilayah", "level": "N2", "example": "土地の面積を正確に測量した。", "example_reading": "とちのめんせきをせいかくにそくりょうした。", "example_meaning": "Mengukur luas area tanah secara akurat."}
])

add_kanji(9, "噺", "シン", "はなし", "Cerita mendongeng dongeng rakugo", [
    {"word": "昔噺", "furigana": "むかしばなし", "romaji": "mukashibanashi", "meaning": "Cerita dongeng rakyat tempo dulu", "level": "N2", "example": "祖母が囲炉裏端で昔噺を聞かせてくれた。", "example_reading": "そぼがいりりばたでむかしばなしをきかせてくれた。", "example_meaning": "Nenek menceritakan dongeng masa lalu di dekat perapian irori."},
    {"word": "噺家", "furigana": "はなしか", "romaji": "hanashika", "meaning": "Pendongeng komedi tradisional rakugo", "level": "N1", "example": "有名な噺家の独演会を見に行く。", "example_reading": "ゆうめいなはなしかのどくえんかいをみにいく。", "example_meaning": "Pergi menonton pertunjukan solo pendongeng komedi rakugo terkenal."},
    {"word": "落語噺", "furigana": "らくごばなし", "romaji": "rakugobanashi", "meaning": "Kisah cerita humor rakugo Jepang", "level": "Umum", "example": "古典の落語噺を聞いて思わず吹き出した。", "example_reading": "こてんのらくごばなしをきいておもわずふきだした。", "example_meaning": "Spontan tertawa terbahak-bahak saat mendengarkan kisah komedi klasik rakugo."}
])

add_kanji(9, "継", "ケイ", "つ・ぐ", "Meneruskan menyambung suksesi", [
    {"word": "継続", "furigana": "けいぞく", "romaji": "keizoku", "meaning": "Keberlanjutan terus menerus konsisten", "level": "N2", "example": "継続は力なりという諺を胸に刻む。", "example_reading": "けいぞくはちからなりということわざをむねにきざむ。", "example_meaning": "Mematri peribahasa 'konsistensi adalah kunci kekuatan' di dalam dada."},
    {"word": "後継", "furigana": "こうけい", "romaji": "koukei", "meaning": "Penerus suksesi generasi pelanjut", "level": "N1", "example": "事業の後継者を育成するプログラムだ。", "example_reading": "じぎょうのこうけいしゃをいくせいするぷろぐらむだ。", "example_meaning": "Program untuk membina mencetak generasi penerus bisnis."},
    {"word": "中継", "furigana": "ちゅうけい", "romaji": "chuukei", "meaning": "Siaran langsung relay transmisi siaran", "level": "N2", "example": "サッカーの決勝戦を生中継で応援する。", "example_reading": "さっかーのけっしょうせんをなまちゅうけいでおうえんする。", "example_meaning": "Mendukung tim dalam siaran langsung pertandingan final sepak bola."}
])

add_kanji(9, "露", "ロ、ロウ", "つゆ", "Embun, terbuka, mengungkap", [
    {"word": "露出", "furigana": "ろしゅつ", "romaji": "roshutsu", "meaning": "Paparan terbuka keterbukaan eksposur", "level": "N1", "example": "メディアへの露出が増えて知名度が上がった。", "example_reading": "めでぃあへのろしゅつがふえてちめいどがあがった。", "example_meaning": "Popularitasnya meningkat berkat bertambahnya eksposur di media massa."},
    {"word": "露天", "furigana": "ろてん", "romaji": "roten", "meaning": "Terbuka di luar ruangan alam terbuka lapak", "level": "N2", "example": "雪景色を眺めながら露天風呂に入る。", "example_reading": "ゆきげしきをながめながらろてんぶろにはいる。", "example_meaning": "Berendam di pemandian air panas terbuka sambil menikmati pemandangan salju."},
    {"word": "披露", "furigana": "ひろう", "romaji": "hirou", "meaning": "Mengumumkan mempertunjukkan memamerkan", "level": "N2", "example": "パーティーで特技のピアノを披露した。", "example_reading": "ぱーてぃーでとくぎのぴあのをひろうした。", "example_meaning": "Mempertunjukkan kepiawaian bermain piano di pesta."}
])

add_kanji(9, "豊", "ホウ", "ゆた・か", "Melimpah ruah makmur kaya raya", [
    {"word": "豊富", "furigana": "ほうふ", "romaji": "houfu", "meaning": "Melimpah ruah banyak kaya akan variasi", "level": "N2", "example": "この図書館には豊富な蔵書が揃っている。", "example_reading": "このとしょかんにはほうふなぞうしょがそろっている。", "example_meaning": "Perpustakaan ini menyediakan koleksi buku yang sangat melimpah."},
    {"word": "豊作", "furigana": "ほうさく", "romaji": "housaku", "meaning": "Panen raya berlimpah hasil bumi sukses", "level": "N2", "example": "今年は天候に恵まれて米が豊作だった。", "example_reading": "ことしはてんこうにめぐまれてこめがほうさくだった。", "example_meaning": "Tahun ini cuaca sangat bagus sehingga panen padi melimpah raya."},
    {"word": "豊か", "furigana": "ゆたか", "romaji": "yutaka", "meaning": "Kaya makmur sejahtera subur", "level": "N3", "example": "自然豊かな村で穏やかに暮らす。", "example_reading": "しぜんゆたかなむらでおだやかにくらす。", "example_meaning": "Hidup tenteram damai di desa yang kaya akan keindahan alam."}
])

add_kanji(9, "就", "シュウ、ジュ", "つ・く、つ・ける", "Menjabat mulai kerja tidur", [
    {"word": "就職", "furigana": "しゅうしょく", "romaji": "shuushoku", "meaning": "Mendapatkan pekerjaan masuk ke dunia kerja", "level": "N3", "example": "希望していたIT企業への就職が決まった。", "example_reading": "きぼうしていたあいてぃーきぎょうへのしゅうしょくがきまった。", "example_meaning": "Dipastikan diterima bekerja di perusahaan IT yang diidam-idamkan."},
    {"word": "就任", "furigana": "しゅうにん", "romaji": "shuunin", "meaning": "Pelantikan pengangkatan memangku jabatan", "level": "N2", "example": "新しい学長に就任した教授の挨拶。", "example_reading": "あたらしいがくちょうにしゅうにんしたきょうじゅのあいさつ。", "example_meaning": "Sambutan pidato dari profesor yang dilantik menjadi rektor baru."},
    {"word": "就寝", "furigana": "しゅうしん", "romaji": "shuushin", "meaning": "Pergi tidur waktu istirahat malam", "level": "N2", "example": "就寝前のスマホ利用は睡眠の質を下げる。", "example_reading": "しゅうしんまえのすまほりようはすいみんのしつをさげる。", "example_meaning": "Menggunakan smartphone sebelum tidur dapat menurunkan kualitas tidur."}
])

add_kanji(9, "防", "ボウ", "ふせ・ぐ", "Mencegah menangkis melindungi", [
    {"word": "予防", "furigana": "よぼう", "romaji": "yobou", "meaning": "Pencegahan preventif antisipasi", "level": "N3", "example": "風邪の予防のためにうがいと手洗いをする。", "example_reading": "かぜのよぼうのためにうがいとてあらいをする。", "example_meaning": "Berkumur dan mencuci tangan demi pencegahan flu batuk."},
    {"word": "防止", "furigana": "ぼうし", "romaji": "boushi", "meaning": "Penanggulangan pencegahan bahaya", "level": "N2", "example": "再発防止のためのルールを徹底する。", "example_reading": "さいはつぼうしのためのるーるをてっていする。", "example_meaning": "Menerapkan aturan secara ketat demi mencegah terjadinya insiden berulang."},
    {"word": "消防", "furigana": "しょうぼう", "romaji": "shoubou", "meaning": "Pemadam kebakaran penanggulangan api", "level": "N3", "example": "消防車がサイレンを鳴らして現場へ急行した。", "example_reading": "しょうぼうしゃがさいれんをならしてげんばへきゅうこうした。", "example_meaning": "Mobil pemadam kebakaran melaju kencang membunyikan sirine ke lokasi."}
])

add_kanji(9, "詐", "サ", "いつわ・る", "Menipu tipu muslihat pura-pura", [
    {"word": "詐欺", "furigana": "さぎ", "romaji": "sagi", "meaning": "Penipuan tindak kriminal penipuan", "level": "N2", "example": "振り込め詐欺の手口に注意するよう呼びかける。", "example_reading": "ふりこめさぎのてぐちにちゅういするようよびかける。", "example_meaning": "Mengimbau masyarakat untuk mewaspadai modus penipuan transfer uang."},
    {"word": "詐称", "furigana": "さしょう", "romaji": "sashou", "meaning": "Mengaku-aku palsu memalsukan identitas", "level": "N1", "example": "学歴を詐称していたことが発覚した。", "example_reading": "がくれきをさしょうしていたことがはっかくした。", "example_meaning": "Terbongkar bahwa ia telah memalsukan riwayat pendidikannya."},
    {"word": "詐術", "furigana": "さじゅつ", "romaji": "sajutsu", "meaning": "Tipu muslihat siasat licik manipulasi", "level": "N1", "example": "巧妙な詐術に引っかかって大金を失った。", "example_reading": "こうみょうなさじゅつにひっかかってたいきんをうしなった。", "example_meaning": "Kehilangan banyak uang karena terjerat muslihat tipuan yang lihai."}
])

add_kanji(9, "欺", "ギ", "あざむ・く", "Mengelabui membohongi memperdaya", [
    {"word": "詐欺", "furigana": "さぎ", "romaji": "sagi", "meaning": "Penipuan kejahatan tipu menipu", "level": "N2", "example": "ネット詐欺の被害に遭わないようパスワードを強化する。", "example_reading": "ねっとさぎのひがいにあわないようぱすわーどをきょうかする。", "example_meaning": "Memperkuat kata sandi agar tidak menjadi korban penipuan internet."},
    {"word": "欺瞞", "furigana": "ぎまん", "romaji": "giman", "meaning": "Pengelabuan kebohongan manipulasi fakta", "level": "N1", "example": "国民を欺瞞するような政治演説に怒りを覚える。", "example_reading": "こくみんをぎまんするようなせいじえんぜつにいかりをおぼえる。", "example_meaning": "Merasa geram atas pidato politik yang mengelabui membohongi rakyat."}
])

add_kanji(9, "順", "ジュン", "", "Urutan lancar tertib patuh", [
    {"word": "順番", "furigana": "じゅんばん", "romaji": "jumban", "meaning": "Giliran urutan nomor urut", "level": "N3", "example": "列に並んで順番を待つ。", "example_reading": "れつにならんでじゅんばんをまつ。", "example_meaning": "Mengantre di barisan dan menunggu giliran."},
    {"word": "順調", "furigana": "じゅんちょう", "romaji": "junchou", "meaning": "Lancar baik tanpa hambatan", "level": "N3", "example": "工事は予定通り順調に進んでいる。", "example_reading": "こうじはよていどおりじゅんちょうにすすんでいる。", "example_meaning": "Pekerjaan konstruksi berjalan lancar sesuai rencana."},
    {"word": "手順", "furigana": "てじゅん", "romaji": "tejun", "meaning": "Tata cara langkah prosedur kerja", "level": "N2", "example": "マニュアルの手順に従って機械を操作する。", "example_reading": "まにゅあるのてじゅんにしたがってきかいをそうさする。", "example_meaning": "Mengoperasikan mesin sesuai langkah prosedur di buku manual."}
])

add_kanji(9, "躍", "ヤク", "おど・る", "Melompat melonjak aktif", [
    {"word": "活躍", "furigana": "かつやく", "romaji": "katsuyaku", "meaning": "Kiprah sukses aktivitas berprestasi", "level": "N3", "example": "世界を舞台に大活躍する若手選手だ。", "example_reading": "せかいをぶたいにだいかつやくするわかてせんしゅだ。", "example_meaning": "Atlet muda yang berkiprah sangat sukses di kancah dunia."},
    {"word": "飛躍", "furigana": "ひやく", "romaji": "hiyaku", "meaning": "Lompatan kemajuan drastis pesat", "level": "N1", "example": "新技術によって産業が飛躍的に発展した。", "example_reading": "しんぎじゅつによってさんぎょうがひやくてきにはってんした。", "example_meaning": "Industri berkembang dengan lompatan drastis berkat teknologi baru."},
    {"word": "躍進", "furigana": "やくしん", "romaji": "yakushin", "meaning": "Langkah terobosan maju meroket pesat", "level": "N1", "example": "アジア市場での目覚ましい躍進を遂げた。", "example_reading": "あじあしじょうでのめざましいやくしんをとげた。", "example_meaning": "Mencatatkan langkah terobosan kemajuan yang pesat di pasar Asia."}
])

add_kanji(9, "漠", "バク", "", "Gurun pasir, samar luas", [
    {"word": "砂漠", "furigana": "さばく", "romaji": "sabaku", "meaning": "Padang pasir gurun gersang", "level": "N3", "example": "砂漠のオアシスでラクダが水を飲む。", "example_reading": "さばくのおあしすでらくだがみずをのむ。", "example_meaning": "Unta minum air di mata air oasis padang pasir."},
    {"word": "漠然", "furigana": "ばくぜん", "romaji": "bakuzen", "meaning": "Samar-samar tidak jelas belum pasti", "level": "N1", "example": "将来について漠然と考えている。", "example_reading": "しょうらいについてばくぜんとかんがえている。", "example_meaning": "Memikirkan masa depan secara samar-samar tanpa rencana pasti."},
    {"word": "広漠", "furigana": "こうばく", "romaji": "koubaku", "meaning": "Luas membentang tak berujung", "level": "N1", "example": "広漠たる大草原を馬で駆け抜ける。", "example_reading": "こうばくたるだいそうげんをうまでかけぬける。", "example_meaning": "Memacu kuda melintasi padang rumput raya yang luas membentang."}
])

add_kanji(9, "梅", "バイ", "うめ", "Pohon plum ume buah prem", [
    {"word": "梅雨", "furigana": "つゆ", "romaji": "tsuyu", "meaning": "Musim hujan tahunan di Jepang (awal musim panas)", "level": "N3", "example": "六月に入ると日本各地で梅雨が始まる。", "example_reading": "ろくがつにはいるとにほんかくちでつゆがはじまる。", "example_meaning": "Memasuki bulan Juni musim hujan (tsuyu) dimulai di berbagai pelosok Jepang."},
    {"word": "梅干し", "furigana": "うめぼし", "romaji": "umeboshi", "meaning": "Asinan buah prem plum umeboshi asam gurih", "level": "N3", "example": "日の丸弁当の真ん中に梅干しを乗せる。", "example_reading": "ひのまるべんとうのまんなかにうめぼしをのせる。", "example_meaning": "Meletakkan umeboshi di tengah-tengah bekal bento Hinomaru."},
    {"word": "塩梅", "furigana": "あんばい", "romaji": "ambai", "meaning": "Takaran bumbu rasa / kondisi keadaan tubuh", "level": "N1", "example": "料理の塩梅がちょうど良くて美味しい。", "example_reading": "りょうりのあんばいがちょうどよくておいしい。", "example_meaning": "Takaran bumbu masakannya pas sekali dan sangat lezat."}
])

# ==========================================
# MINGGU 10 (25 Kanji)
# 邦、奏、授、厄、徹、俵、故、郷、離、殊、悟、響、患、添、録、毒、延、詩、沸、激、騒、枠、掛、刻、柄
# ==========================================
add_kanji(10, "邦", "ホウ", "くに", "Negeri, tanah air bangsa, Jepang", [
    {"word": "邦画", "furigana": "ほうが", "romaji": "houga", "meaning": "Film produksi perfilman Jepang", "level": "N2", "example": "映画館で最新の邦画を鑑賞した。", "example_reading": "えいがかんでさいしんのほうがをかんしょうした。", "example_meaning": "Menonton film Jepang terbaru di bioskop."},
    {"word": "連邦", "furigana": "れんぽう", "romaji": "rempou", "meaning": "Federasi negara serikat perserikatan", "level": "N1", "example": "連邦議会で新しい法案が可決された。", "example_reading": "れんぽうぎかいであたらしいほうあんがかけつされた。", "example_meaning": "Rancangan undang-undang baru disahkan di parlemen federal."},
    {"word": "本邦", "furigana": "ほんぽう", "romaji": "hompou", "meaning": "Negeri ini / tanah air (Jepang)", "level": "N1", "example": "本邦初公開の貴重な美術品だ。", "example_reading": "ほんぽうはつこうかいのきちょうなびじゅつひんだ。", "example_meaning": "Karya seni berharga yang pertama kalinya dipamerkan di negeri ini."}
])

add_kanji(10, "奏", "ソウ", "かな・でる", "Memainkan instrumen musik melantunkan", [
    {"word": "演奏", "furigana": "えんそう", "romaji": "ensou", "meaning": "Pertunjukan musik memainkan alat musik", "level": "N3", "example": "ピアノの生演奏に会場が聞き惚れた。", "example_reading": "ぴあののなまえんそうにかいじょうがききほれた。", "example_meaning": "Seluruh hadirin terpesona mendengarkan permainan piano secara langsung."},
    {"word": "合奏", "furigana": "がっそう", "romaji": "gassou", "meaning": "Ensambel musik orkestrasi instrumen bersama", "level": "N2", "example": "ヴァイオリンとフルートの合奏を楽しむ。", "example_reading": "ゔぁいおりんとふるーとのがっそうをたのしむ。", "example_meaning": "Menikmati permainan ansambel musik biola dan seruling."},
    {"word": "伴奏", "furigana": "ばんそう", "romaji": "bansou", "meaning": "Iringan musik mengiringi nyanyian", "level": "N1", "example": "合唱のピアノ伴奏を務めた。", "example_reading": "がっしょうのぴあのばんそうをつとめた。", "example_meaning": "Bertugas mengiringi nyanyian paduan suara dengan piano."}
])

add_kanji(10, "授", "ジュ", "さず・ける、さず・かる", "Mengajar memberi menganugerahi", [
    {"word": "授業", "furigana": "じゅぎょう", "romaji": "jugyou", "meaning": "Pelajaran jam belajar di kelas", "level": "N4", "example": "明日の日本語の授業の予習をする。", "example_reading": "あしたのにほんごのじゅぎょうのよしゅうをする。", "example_meaning": "Mempersiapkan materi pelajaran bahasa Jepang untuk besok."},
    {"word": "教授", "furigana": "きょうじゅ", "romaji": "kyouju", "meaning": "Profesor guru besar universitas", "level": "N2", "example": "大学の教授から研究の指導を受ける。", "example_reading": "だいがくのきょうじゅからけんきゅうのしどうをうける。", "example_meaning": "Mendapat bimbingan penelitian dari profesor universitas."},
    {"word": "授与", "furigana": "じゅよ", "romaji": "juyo", "meaning": "Penganugerahan penyerahan piagam ijazah", "level": "N1", "example": "卒業式で卒業証書が授与された。", "example_reading": "そつぎょうしきでそつぎょうしょうしょがじゅよされた。", "example_meaning": "Ijazah kelulusan diserahkan pada upacara wisuda kelulusan."}
])

add_kanji(10, "厄", "ヤク", "", "Bencana kemalangan kerepotan sial", [
    {"word": "厄介", "furigana": "やっかい", "romaji": "yakkai", "meaning": "Merepotkan masalah pelik beban", "level": "N2", "example": "厄介な問題に巻き込まれてしまった。", "example_reading": "やっかいなもんだいにまきこまれてしまった。", "example_meaning": "Terbawa terseret ke dalam masalah yang sangat pelik merepotkan."},
    {"word": "厄年", "furigana": "やくどし", "romaji": "yakudoshi", "meaning": "Tahun rawan sial dalam kepercayaan Jepang", "level": "Umum", "example": "厄年の厄除けにお寺へ参拝した。", "example_reading": "やくどしのやくよけにおてらへさんぱいした。", "example_meaning": "Berdoa ke kuil untuk tolak bala di tahun rawan sial (yakudoshi)."},
    {"word": "災厄", "furigana": "さいやく", "romaji": "saiyaku", "meaning": "Bencana kemalangan malapetaka", "level": "N1", "example": "不慮の災厄から身を守る心構え。", "example_reading": "ふりょのさいやくからみをまもるこころがまえ。", "example_meaning": "Kesiapan mental untuk melindungi diri dari bencana kemalangan tak terduga."}
])

add_kanji(10, "徹", "テツ", "", "Tuntas tembus menyeluruh semalaman", [
    {"word": "徹底", "furigana": "てってい", "romaji": "tettei", "meaning": "Tuntas menyeluruh konsisten tanpa kompromi", "level": "N2", "example": "衛生管理を徹底して感染を防ぐ。", "example_reading": "えいせいかんりをてっていしてかんせんをふせぐ。", "example_meaning": "Menjaga sanitasi kebersihan secara tuntas untuk mencegah penularan."},
    {"word": "徹夜", "furigana": "てつや", "romaji": "tetsuya", "meaning": "Begadang semalaman semalam suntuk", "level": "N3", "example": "試験勉強のために昨夜は徹夜した。", "example_reading": "しけんべんきょうのためにさくやはてつやした。", "example_meaning": "Semalam suntuk saya begadang demi belajar untuk ujian."},
    {"word": "徹頭徹尾", "furigana": "てっとうてつび", "romaji": "tettoutetsubi", "meaning": "Dari awal sampai akhir secara konsisten menyeluruh", "level": "N1", "example": "徹頭徹尾、自らの信念を貫き通した。", "example_reading": "てっとうてつび、みずからのしんねんをつらぬきとおした。", "example_meaning": "Dari awal sampai akhir secara konsisten memegang teguh keyakinan diri."}
])

add_kanji(10, "俵", "ヒョウ", "たわら", "Karung jerami beras, arena sumo", [
    {"word": "土俵", "furigana": "どひょう", "romaji": "dohyou", "meaning": "Arena gelanggang pertandingan sumo", "level": "N1", "example": "力士が土俵の上で激しくぶつかり合う。", "example_reading": "りきしがどひょうのうえではげしくぶつかりあう。", "example_meaning": "Para pesumo saling bertubrukan sengit di atas arena gelanggang dohyo."},
    {"word": "米俵", "furigana": "こめだわら", "romaji": "komedawara", "meaning": "Karung jerami tempat beras tradisional", "level": "Umum", "example": "昔は収穫した米を米俵に詰めて運んだ。", "example_reading": "むかしはしゅうかくしたこめをこめだわらにつめてはこんだ。", "example_meaning": "Zaman dahulu beras yang dipanen dimasukkan ke dalam karung jerami lalu diangkut."}
])

add_kanji(10, "故", "コ", "ゆえ", "Sebab akibat, rusak, almarhum, sengaja", [
    {"word": "事故", "furigana": "じこ", "romaji": "jiko", "meaning": "Kecelakaan musibah insiden", "level": "N4", "example": "交通事故に気をつけて安全運転を心がける。", "example_reading": "こうつうじこにきをつけてあんぜんうんてんをこころがける。", "example_meaning": "Hati-hati terhadap kecelakaan lalu lintas dan utamakan keselamatan berkendara."},
    {"word": "故障", "furigana": "こしょう", "romaji": "koshou", "meaning": "Kerusakan macet mesin alat", "level": "N3", "example": "エアコンが故障して冷風が出ない。", "example_reading": "えあこんがこしょうしてれいふうがでない。", "example_meaning": "AC rusak dan tidak mengeluarkan hawa dingin."},
    {"word": "故意", "furigana": "こい", "romaji": "koi", "meaning": "Kesengajaan secara sengaja diniatkan", "level": "N1", "example": "故意にルールを破ったわけではない。", "example_reading": "こいにるーるをやぶったわけではない。", "example_meaning": "Bukan berarti sengaja melanggar aturan tersebut."},
    {"word": "故郷", "furigana": "こきょう", "romaji": "kokyou", "meaning": "Kampung halaman tanah kelahiran", "level": "N3", "example": "お正月に故郷へ帰省した。", "example_reading": "おしょうがつにこきょうへきせいした。", "example_meaning": "Mudik pulang ke kampung halaman saat libur tahun baru."}
])

add_kanji(10, "郷", "キョウ、ゴウ", "さと", "Kampung desa daerah asal", [
    {"word": "故郷", "furigana": "こきょう", "romaji": "kokyou", "meaning": "Kampung halaman tanah kelahiran", "level": "N3", "example": "懐かしい故郷の風景を思い出す。", "example_reading": "なつかしいこきょうのふうけいをおもいだす。", "example_meaning": "Teringat kembali pemandangan kampung halaman yang kurindukan."},
    {"word": "郷土", "furigana": "きょうど", "romaji": "kyoudo", "meaning": "Daerah lokal tradisional kearifan lokal", "level": "N1", "example": "旅行先で美味しい郷土料理を味わった。", "example_reading": "りょこうさきでおいしいきょうどりょうりをあじわった。", "example_meaning": "Mencicipi masakan tradisional daerah setempat di tempat wisata."},
    {"word": "帰郷", "furigana": "ききょう", "romaji": "kikyou", "meaning": "Kepulangan kembali ke kampung halaman mudik", "level": "N1", "example": "仕事を辞めて地方へ帰郷することを決意した。", "example_reading": "しごとをやめてちほうへききょうすることをけついした。", "example_meaning": "Memutuskan berhenti kerja dan kembali pulang ke kampung halaman di daerah."}
])

add_kanji(10, "離", "リ", "はな・れる、はな・す", "Berpisah menjauh lepas jarak", [
    {"word": "距離", "furigana": "きょり", "romaji": "kyori", "meaning": "Jarak bentang kejauhan", "level": "N3", "example": "東京から大阪までの距離を調べる。", "example_reading": "とうきょうからおおさかまでのきょりをしらべる。", "example_meaning": "Mencari tahu jarak dari Tokyo hingga ke Osaka."},
    {"word": "離婚", "furigana": "りこん", "romaji": "rikon", "meaning": "Perceraian perpisahan pernikahan", "level": "N2", "example": "お互いに納得して円満に離婚した。", "example_reading": "おたがいになっとくしてえんまんにりこんした。", "example_meaning": "Keduanya sepakat dan berpisah cerai secara baik-baik."},
    {"word": "隔離", "furigana": "かくり", "romaji": "kakuri", "meaning": "Isolasi karantina pemisahan sterilisasi", "level": "N1", "example": "感染症の拡大を防ぐため患者を隔離した。", "example_reading": "かんせんしょうのかくだいをふせぐためかんじゃをかくりした。", "example_meaning": "Pasien diisolasi demi mencegah perluasan penyakit menular."},
    {"word": "離陸", "furigana": "りりく", "romaji": "ririku", "meaning": "Lepas landas pesawat terbang take-off", "level": "N2", "example": "飛行機が無事に滑走路から離陸した。", "example_reading": "ひこうきがぶじにかっそうろからりりくした。", "example_meaning": "Pesawat terbang berhasil lepas landas dengan selamat dari landasan pacu."}
])

add_kanji(10, "殊", "シュ", "こと", "Istimewa berbeda khusus", [
    {"word": "特殊", "furigana": "とくしゅ", "romaji": "tokushu", "meaning": "Khusus istimewa spesifik unik", "level": "N2", "example": "特殊な素材を使って頑丈な製品を作る。", "example_reading": "とくしゅなそざいをつかってがんじょうなせいひんをつくる。", "example_meaning": "Membuat produk yang kokoh menggunakan material bahan khusus."},
    {"word": "殊更", "furigana": "ことさら", "romaji": "kotosara", "meaning": "Secara sengaja khusus dibuat-buat", "level": "N1", "example": "殊更に問題を大きくする必要はない。", "example_reading": "ことさらにもんだいをおおきくするひつようはない。", "example_meaning": "Tidak perlu membesar-besarkan masalah secara sengaja."},
    {"word": "殊勲", "furigana": "しゅくん", "romaji": "shukun", "meaning": "Jasa besar prestasi gemilang luar biasa", "level": "N1", "example": "決勝ゴールを決めて殊勲賞を受賞した。", "example_reading": "けっしょうごーるをきめてしゅくんしょうをじゅしょうした。", "example_meaning": "Mencetak gol kemenangan penentu dan meraih anugerah jasa luar biasa."}
])

add_kanji(10, "悟", "ゴ", "さと・る", "Sadar pencerahan paham tekad", [
    {"word": "覚悟", "furigana": "かくご", "romaji": "kakugo", "meaning": "Kesiapan mental tekad bulat menerima risiko", "level": "N2", "example": "どんな困難も乗り越える覚悟を決めた。", "example_reading": "どんなこんなんものりこえるかくごをきめた。", "example_meaning": "Memantapkan tekad kesiapan batin untuk mengatasi kesulitan apa pun."},
    {"word": "悟り", "furigana": "さとり", "romaji": "satori", "meaning": "Pencerahan spiritual pemahaman batin", "level": "N1", "example": "長い瞑想の末に悟りを開いた。", "example_reading": "ながいめいそうのすえにさとりをひらいた。", "example_meaning": "Mencapai pencerahan batin setelah meditasi yang panjang."},
    {"word": "改悟", "furigana": "かいご", "romaji": "kaigo", "meaning": "Bertaubat dan menyadari kesalahan sendiri", "level": "N1", "example": "自らの非を改悟して一からやり直す。", "example_reading": "みずからのひをかいごしていちからやりなおす。", "example_meaning": "Menyadari kesalahan diri dan memulai kembali dari nol."}
])

add_kanji(10, "響", "キョウ", "ひび・く", "Gema gaung getaran bunyi imbas", [
    {"word": "影響", "furigana": "えいきょう", "romaji": "eikyou", "meaning": "Pengaruh dampak imbas", "level": "N3", "example": "円安が物価に大きな影響を与えている。", "example_reading": "えんやすがぶっかにおおきなえいきょうをあたえている。", "example_meaning": "Pelemahan nilai yen memberi dampak besar terhadap harga kebutuhan pokok."},
    {"word": "反響", "furigana": "はんきょう", "romaji": "hankyou", "meaning": "Reaksi tanggapan gema publik", "level": "N1", "example": "発表された新製品は市場で大きな反響を呼んだ。", "example_reading": "はっぴょうされたしんせいひんはしじょうでおおきなはんきょうをよんだ。", "example_meaning": "Produk baru yang diumumkan memicu tanggapan reaksi besar di pasar."},
    {"word": "音響", "furigana": "おんきょう", "romaji": "onkyou", "meaning": "Tata akustik efek tata suara", "level": "N1", "example": "最新の音響システムで映画の臨場感を楽しむ。", "example_reading": "さいしんのおんきょうしすてむでえいがのりんじょうかんをたのしむ。", "example_meaning": "Menikmati sensasi nyata film dengan sistem tata suara akustik mutakhir."}
])

add_kanji(10, "患", "カン", "わずら・う", "Penyakit derita pasien terjangkit", [
    {"word": "患者", "furigana": "かんじゃ", "romaji": "kanja", "meaning": "Pasien orang yang berobat sakit", "level": "N3", "example": "医師が親切に患者の話を聞く。", "example_reading": "いしがしんせつにかんじゃのはなしをきく。", "example_meaning": "Dokter mendengarkan keluhan pasien dengan ramah dan sabar."},
    {"word": "急患", "furigana": "きゅうかん", "romaji": "kyuukan", "meaning": "Pasien gawat darurat", "level": "N1", "example": "夜間病院に急患が次々と運び込まれた。", "example_reading": "やかんびょういんにきゅうかんがつぎつぎとはこびこまれた。", "example_meaning": "Pasien darurat dilarikan berturut-turut ke rumah sakit malam hari."},
    {"word": "疾患", "furigana": "しっかん", "romaji": "shikkan", "meaning": "Penyakit medis gangguan klinis", "level": "N1", "example": "心臓の疾患を早期に発見して治療する。", "example_reading": "しんぞうのしっかんをそうきにはっけんしてちりょうする。", "example_meaning": "Mendeteksi dan mengobati penyakit jantung sedini mungkin."}
])

add_kanji(10, "添", "テン", "そ・える", "Melampirkan menyertakan", [
    {"word": "添付", "furigana": "てんぷ", "romaji": "tempu", "meaning": "Lampiran dokumen berkas email", "level": "N2", "example": "添付ファイルを開いて内容を確認してください。", "example_reading": "てんぷふぁいるをひらいてないようをかくにんしてください。", "example_meaning": "Silakan buka berkas lampiran dan pastikan isinya."},
    {"word": "添削", "furigana": "てんさく", "romaji": "tensaku", "meaning": "Koreksi penyuntingan tugas tulisan", "level": "N1", "example": "日本語のレポートを先生に添削してもらった。", "example_reading": "にほんごのれぽーとをせんせいにてんさくしてもらった。", "example_meaning": "Laporan bahasa Jepang saya dikoreksi oleh guru."}
])

add_kanji(10, "録", "ロク", "", "Merekam mencatat daftar log", [
    {"word": "記録", "furigana": "きろく", "romaji": "kiroku", "meaning": "Rekor catatan dokumentasi riwayat", "level": "N3", "example": "大会で世界新記録が樹立された。", "example_reading": "たいかいでせかいしんきろくがじゅりつされた。", "example_meaning": "Rekor dunia baru berhasil dicetak dalam kompetisi."},
    {"word": "登録", "furigana": "とうろく", "romaji": "touroku", "meaning": "Pendaftaran registrasi resmi", "level": "N3", "example": "ウェブサイトで会員登録を済ませた。", "example_reading": "うぇぶさいとでかいいんとうろくをすませた。", "example_meaning": "Menyelesaikan pendaftaran akun keanggotaan di situs web."},
    {"word": "録音", "furigana": "ろくおん", "romaji": "rokuon", "meaning": "Perekaman suara rekaman audio", "level": "N3", "example": "インタビューの音声をボイスレコーダーに録音した。", "example_reading": "いんたびゅーのおんせいをぼいすれこーだーにろくおんした。", "example_meaning": "Merekam suara wawancara ke dalam perekam audio."},
    {"word": "収録", "furigana": "しゅうろく", "romaji": "shuuroku", "meaning": "Perekaman syuting / termuat dalam buku", "level": "N1", "example": "テレビ番組のスタジオ収録に参加した。", "example_reading": "てれびばんぐみのすたじおしゅうろくにしさんかした。", "example_meaning": "Ikut serta dalam syuting rekaman studio program televisi."}
])

add_kanji(10, "毒", "ドク", "", "Racun zat beracun adiksi", [
    {"word": "中毒", "furigana": "ちゅうどく", "romaji": "chuudoku", "meaning": "Keracunan / kecanduan adiksi", "level": "N2", "example": "夏場は食中毒に十分に気をつける必要がある。", "example_reading": "なつばはしょくちゅうどくにじゅうぶんにきをつけるひつようがある。", "example_meaning": "Perlu berhati-hati ekstra terhadap keracunan makanan di musim panas."},
    {"word": "消毒", "furigana": "しょうどく", "romaji": "shoudoku", "meaning": "Disinfeksi sterilisasi pembersihan kuman", "level": "N3", "example": "アルコールで手指を消毒する。", "example_reading": "あるこーるでしゅしをしょうどくする。", "example_meaning": "Mendisinfeksi jari-jemari tangan dengan alkohol."},
    {"word": "毒舌", "furigana": "どくぜつ", "romaji": "dokuzetsu", "meaning": "Lidah tajam ucapan pedas menyengat", "level": "N1", "example": "彼の毒舌トークはテレビで大人気だ。", "example_reading": "かれのどくぜつとーくはてれびでだいにんきだ。", "example_meaning": "Bicaranya yang berlidah tajam pedas sangat populer di televisi."}
])

add_kanji(10, "延", "エン", "の・びる、の・ばす", "Memperpanjang menunda molor", [
    {"word": "延長", "furigana": "えんちょう", "romaji": "enchou", "meaning": "Perpanjangan waktu durasi", "level": "N2", "example": "ビザの滞在期間を延長する手続きを行う。", "example_reading": "びざのたいざいきかんをえんちょうするてつづきをおこなう。", "example_meaning": "Mengurus prosedur perpanjangan masa tinggal visa."},
    {"word": "延期", "furigana": "えんき", "romaji": "enki", "meaning": "Penundaan pengunduran jadwal", "level": "N2", "example": "大雨のため運動会が来週に延期された。", "example_reading": "おおあめのためうんどうかいがらいしゅうにえんきされた。", "example_meaning": "Lomba olahraga diundur ke minggu depan akibat hujan lebat."},
    {"word": "遅延", "furigana": "ちえん", "romaji": "chien", "meaning": "Keterlambatan delay jadwal kereta/pesawat", "level": "N1", "example": "信号トラブルにより電車の遅延が発生した。", "example_reading": "しんごうとらぶるによりでんしゃのちえんがはっせいした。", "example_meaning": "Terjadi keterlambatan kereta akibat gangguan persinyalan."}
])

add_kanji(10, "詩", "シ", "うた", "Puisi sajak bait pantun", [
    {"word": "詩人", "furigana": "しじん", "romaji": "shijin", "meaning": "Penyair pujangga pembuat sajak", "level": "N3", "example": "有名な詩人の代表作を朗読する。", "example_reading": "ゆうめいなしじんのだいひょうさくをろうどくする。", "example_meaning": "Mendeklamasikan karya utama penyair ternama."},
    {"word": "詩集", "furigana": "ししゅう", "romaji": "shishuu", "meaning": "Antologi kumpulan buku puisi", "level": "N2", "example": "古本屋で懐かしい詩集を見つけた。", "example_reading": "ふるほんやでなつかしいししゅうをみつけた。", "example_meaning": "Menemukan antologi kumpulan puisi bernostalgia di toko buku bekas."},
    {"word": "漢詩", "furigana": "かんし", "romaji": "kanshi", "meaning": "Puisi klasik tradisi aksara Tiongkok", "level": "N1", "example": "高校の古典の授業で漢詩を学んだ。", "example_reading": "こうこうのこてんのじゅぎょうでかんしをまなんだ。", "example_meaning": "Belajar puisi klasik Tiongkok di pelajaran sastra klasik SMA."}
])

add_kanji(10, "沸", "フツ", "わ・く、わ・かす", "Mendidih memanas bergolak", [
    {"word": "沸騰", "furigana": "ふっとう", "romaji": "futtou", "meaning": "Mendidih menggelegak memuncak", "level": "N2", "example": "お湯が沸騰したら火を止めてください。", "example_reading": "おゆがふっとうしたらひをとめてください。", "example_meaning": "Silakan matikan api jika air sudah mendidih."},
    {"word": "沸点", "furigana": "ふってん", "romaji": "futten", "meaning": "Titik didih derajat didih cairan", "level": "N1", "example": "水の沸点は標準気圧で百度である。", "example_reading": "みずのふってんはひょうじゅんきあつでひゃくどである。", "example_meaning": "Titik didih air pada tekanan standar adalah 100 derajat Celsius."},
    {"word": "煮沸", "furigana": "しゃふつ", "romaji": "shafutsu", "meaning": "Merebus untuk sterilisasi kuman", "level": "N1", "example": "赤ちゃんの哺乳瓶を煮沸消毒する。", "example_reading": "あかちゃんのほにゅうびんをしゃふつしょうどくする。", "example_meaning": "Mensterilisasi botol susu bayi dengan cara direbus air mendidih."}
])

add_kanji(10, "激", "ゲキ", "はげ・しい", "Kencang sengit drastis terharu", [
    {"word": "激励", "furigana": "げきれい", "romaji": "gekirei", "meaning": "Pemberian suntikan kobaran semangat", "level": "N1", "example": "試合前に監督が選手たちを熱く激励した。", "example_reading": "しあいまえにかんとくがせんしゅたちをあつくげきれいした。", "example_meaning": "Pelatih menyuntikkan semangat membara kepada para atlet sebelum tanding."},
    {"word": "感激", "furigana": "かんげき", "romaji": "kangeki", "meaning": "Terharu sangat tersentuh hati mendalam", "level": "N2", "example": "ファンの温かい応援に深く感激した。", "example_reading": "ふぁんのあたたかいおうえんにふかくかんげきした。", "example_meaning": "Sangat terharu mendalam atas dukungan hangat para penggemar."},
    {"word": "激増", "furigana": "げきぞう", "romaji": "gekizou", "meaning": "Lonjakan drastis peningkatan tajam", "level": "N1", "example": "外国人観光客がこの一年で激増した。", "example_reading": "がいこくじんかんこうきゃくがこのいちねんでげきぞうした。", "example_meaning": "Wisatawan mancanegara melonjak drastis dalam satu tahun terakhir."},
    {"word": "刺激", "furigana": "しげき", "romaji": "shigeki", "meaning": "Stimulasi rangsangan motivasi", "level": "N2", "example": "友人の成功が良い刺激になった。", "example_reading": "ゆうじんのせいこうがよいしげきになった。", "example_meaning": "Kesuksesan sahabat menjadi dorongan stimulasi yang baik bagi saya."}
])

add_kanji(10, "騒", "ソウ", "さわ・ぐ", "Bising gaduh ribut heboh", [
    {"word": "騒音", "furigana": "そうおん", "romaji": "souon", "meaning": "Kebisingan polusi suara bising", "level": "N2", "example": "空港周辺の住民が騒音に悩まされている。", "example_reading": "くうこうしゅうへんのじゅうみんがそうおんになやまされている。", "example_meaning": "Warga di sekitar bandara terganggu oleh polusi kebisingan suara."},
    {"word": "騒動", "furigana": "そうどう", "romaji": "soudou", "meaning": "Keributan huru-hara kekacauan gaduh", "level": "N1", "example": "街中で思わぬ騒動が巻き起こった。", "example_reading": "まちじゅうでおもわぬそうどうがまきおこった。", "example_meaning": "Keributan gaduh tak terduga pecah di tengah kota."},
    {"word": "物騒", "furigana": "ぶっそう", "romaji": "bussou", "meaning": "Rawan berbahaya tidak aman rawan kriminal", "level": "N2", "example": "夜間の一人歩きは物騒だから気をつけなさい。", "example_reading": "やかんのひとりあるきはぶっそうだからきをつけなさい。", "example_meaning": "Jalan sendirian di malam hari rawan berbahaya, jadi berhati-hatilah."}
])

add_kanji(10, "枠", "", "わく", "Bingkai kerangka kuota batas", [
    {"word": "枠組み", "furigana": "わくぐみ", "romaji": "wakugumi", "meaning": "Kerangka kerja framework rancangan dasar", "level": "N1", "example": "国際協力の新しい枠組みを構築する。", "example_reading": "こくさいきょうりょくのあたらしいわくぐみをこうちくする。", "example_meaning": "Membangun kerangka kerja baru bagi kerja sama internasional."},
    {"word": "別枠", "furigana": "べつわく", "romaji": "betsuwaku", "meaning": "Kuota khusus slot tersendiri alokasi terpisah", "level": "N1", "example": "留学生向けの別枠採用を実施する。", "example_reading": "りゅうがくせいむけのべつわくさいようをじっしする。", "example_meaning": "Membuka rekrutmen kuota khusus bagi mahasiswa asing."},
    {"word": "予算枠", "furigana": "よさんわく", "romaji": "yosanwaku", "meaning": "Pagu anggaran batas alokasi anggaran", "level": "N1", "example": "各部署の予算枠を厳格に管理する。", "example_reading": "かくぶしょのよさんわくをげんかくにかんりする。", "example_meaning": "Mengelola pagu anggaran setiap divisi secara ketat."}
])

add_kanji(10, "掛", "カイ", "か・ける、か・かる", "Menggantung kait melibatkan", [
    {"word": "手掛け", "furigana": "てがけ", "romaji": "tegake", "meaning": "Menangani menggarap langsung proyek", "level": "N1", "example": "彼が手掛けた建築デザインが高く評価された。", "example_reading": "かれがてがけたけんちくでざいんがたかくひょうかされた。", "example_meaning": "Desain arsitektur yang digarap langsung olehnya mendapat apresiasi tinggi."},
    {"word": "目掛け", "furigana": "めがけ", "romaji": "megake", "meaning": "Membidik mengincar target sasaran", "level": "N1", "example": "ゴールを目掛けて力強くシュートを放った。", "example_reading": "ごーるをめがけてちからづよくしゅーとをはなった。", "example_meaning": "Melesatkan tendangan keras mengincar gawang lawan."},
    {"word": "掛け金", "furigana": "かけきん", "romaji": "kakekin", "meaning": "Premi asuransi cicilan berkala / gerendel kunci", "level": "N2", "example": "毎月一定の保険の掛け金を支払っている。", "example_reading": "まいつきいっていのかけきんをしはらっている。", "example_meaning": "Membayar premi asuransi dalam jumlah tetap setiap bulan."}
])

add_kanji(10, "刻", "コク", "きざ・む", "Mengukir waktu detik genting", [
    {"word": "深刻", "furigana": "しんこく", "romaji": "shinkoku", "meaning": "Serius parah genting gawat", "level": "N3", "example": "地球温暖化は深刻な問題だ。", "example_reading": "ちきゅうおんだんかはしんこくなどもんだいだ。", "example_meaning": "Pemanasan global adalah masalah yang sangat serius."},
    {"word": "遅刻", "furigana": "ちこく", "romaji": "chikoku", "meaning": "Terlambat datang telat", "level": "N4", "example": "電車が遅れて学校に遅刻した。", "example_reading": "でんしゃがおくれてがっこうにちこくした。", "example_meaning": "Terlambat masuk sekolah karena kereta terlambat."},
    {"word": "彫刻", "furigana": "ちょうこく", "romaji": "choukoku", "meaning": "Seni patung ukiran pahatan", "level": "N2", "example": "木彫りの美しい彫刻を鑑賞した。", "example_reading": "きぼりのうつくしいちょうこくをかんしょうした。", "example_meaning": "Menikmati karya seni patung ukiran kayu yang indah."},
    {"word": "時刻", "furigana": "じこく", "romaji": "jikoku", "meaning": "Waktu jam saat pada jadwal", "level": "N3", "example": "電車の発車時刻をアプリで確認する。", "example_reading": "でんしゃのはっしゃじこくをあぷりでかくにんする。", "example_meaning": "Memeriksa jam keberangkatan kereta lewat aplikasi."}
])

add_kanji(10, "柄", "ヘイ", "がら、え", "Corak motif, watak tabiat, gagang", [
    {"word": "人柄", "furigana": "ひとがら", "romaji": "hitogara", "meaning": "Kepribadian watak pembawaan diri", "level": "N2", "example": "温和な人柄で誰からも好かれている。", "example_reading": "おんわなひとがらでだれからもすかれている。", "example_meaning": "Disukai oleh siapa pun karena kepribadiannya yang ramah lemah lembut."},
    {"word": "家柄", "furigana": "いえがら", "romaji": "iegara", "meaning": "Garis silsilah keluarga martabat keluarga", "level": "N1", "example": "由緒ある古い家柄の出身だ。", "example_reading": "ゆいしょあるふるいいえがらのしゅっしんだ。", "example_meaning": "Berasal dari keluarga terpandang yang memiliki silsilah bersejarah."},
    {"word": "身柄", "furigana": "みがら", "romaji": "migara", "meaning": "Fisik raga seseorang dalam penahanan penyerahan", "level": "N1", "example": "逃走した容疑者の身柄を確保した。", "example_reading": "とうそうしたようぎしゃのみがらをかくほした。", "example_meaning": "Berhasil mengamankan menahan tersangka yang sempat melarikan diri."}
])

# ==========================================
# MINGGU 11 (28 Kanji)
# 誇、漬、煎、吟、銘、駄、豊、富、伐、堪、築、崩、根、拠、沸、著、総、菜、再、帯、救、粧、益、貢、献、判、殖、乏、嘆
# (duplicate 漬 removed)
# ==========================================
add_kanji(11, "誇", "コ", "ほこ・る", "Bangga membanggakan memamerkan", [
    {"word": "誇示", "furigana": "こじ", "romaji": "koji", "meaning": "Unjuk pamer memamerkan kekuatan keunggulan", "level": "N1", "example": "圧倒的な軍事力を誇示するパレード。", "example_reading": "あっとうてきなぐんじりょくをこじするぱれーど。", "example_meaning": "Parade yang memamerkan unjuk kekuatan militer yang luar biasa."},
    {"word": "誇張", "furigana": "こちょう", "romaji": "kochou", "meaning": "Melebih-lebihkan hiperbola dibesar-besarkan", "level": "N1", "example": "話を誇張せずにありのまま報告してください。", "example_reading": "はなしをこちょうせずにあるがままほうこくしてください。", "example_meaning": "Tolong laporkan apa adanya tanpa melebih-lebihkan cerita."},
    {"word": "誇り", "furigana": "ほこり", "romaji": "hokori", "meaning": "Kebanggaan harga diri marwah", "level": "N2", "example": "自分の仕事に誇りを持って取り組む。", "example_reading": "じぶんのしごとにほこりをもってとりくむ。", "example_meaning": "Mengerjakan tugas dengan membawa rasa bangga atas profesinya."}
])

add_kanji(11, "漬", "シ", "つ・ける、つ・かる", "Merendam asinan acar membubuhi", [
    {"word": "漬物", "furigana": "つけもの", "romaji": "tsukemono", "meaning": "Acar asinan sayuran khas Jepang", "level": "N3", "example": "和食の定食には漬物が欠かせない。", "example_reading": "わしょくのていしょくにはつけものがかかせない。", "example_meaning": "Acar asinan sayur tsukemono tak boleh terlewat dalam paket menu makanan Jepang."},
    {"word": "茶漬け", "furigana": "ちゃづけ", "romaji": "chazuke", "meaning": "Nasi siram kuah teh ochazuke", "level": "N2", "example": "夜食にサラサラとお茶漬けを食べる。", "example_reading": "やしょくにさらさらとおちゃづけをたべる。", "example_meaning": "Menikmati seporsi ochazuke yang segar untuk santap malam."},
    {"word": "塩漬け", "furigana": "しおづけ", "romaji": "shiodzuke", "meaning": "Pengasinan diawetkan dengan garam", "level": "N1", "example": "新鮮な魚を塩漬けにして保存食にする。", "example_reading": "しんせんなさかなをしおづけにしてほぞんしょくにする。", "example_meaning": "Mengawetkan ikan segar dengan cara diasinkan untuk cadangan makanan."}
])

add_kanji(11, "煎", "セン", "い・る、せん・じる", "Memanggang menyangrai menyeduh", [
    {"word": "煎茶", "furigana": "せんちゃ", "romaji": "sencha", "meaning": "Teh hijau seduh sencha khas Jepang", "level": "N2", "example": "食後に温かい煎茶を一杯飲んで一息つく。", "example_reading": "しょくごにあたたかいせんちゃをいっぱいのんでひといきつく。", "example_meaning": "Menikmati secangkir teh hijau sencha hangat setelah makan untuk melepas penat."},
    {"word": "焙煎", "furigana": "ばいせん", "romaji": "baisen", "meaning": "Pemanggangan roasting biji kopi teh", "level": "N1", "example": "自家焙煎のこだわりのコーヒーを提供するカフェ。", "example_reading": "じかばいせんのこだわりのこーひーをていきょうするかふぇ。", "example_meaning": "Kafe yang menyajikan kopi pilihan yang disangrai (roasting) sendiri."},
    {"word": "煎餅", "furigana": "せんべい", "romaji": "sembei", "meaning": "Kerupuk beras panggang senbei gurih", "level": "N3", "example": "お茶請けに醤油味の煎餅を食べる。", "example_reading": "おちゃうけにしょうゆあじのせんべいをたべる。", "example_meaning": "Makan kerupuk beras senbei rasa kecap shoyu sebagai camilan teman minum teh."}
])

add_kanji(11, "吟", "ギン", "", "Memilih teliti melantunkan sajak", [
    {"word": "吟味", "furigana": "ぎんみ", "romaji": "gimmi", "meaning": "Pengujian pemilihan teliti saksama", "level": "N1", "example": "素材を厳しく吟味して最高の料理を作る。", "example_reading": "そざいをきびしくぎんみしてさいこうのりょうりをつくる。", "example_meaning": "Memilih bahan secara teliti dan ketat demi menghasilkan masakan terbaik."},
    {"word": "詩吟", "furigana": "しぎん", "romaji": "shigin", "meaning": "Seni melantunkan tembang puisi klasik Jepang", "level": "N1", "example": "祖父が趣味で詩吟の教室に通っている。", "example_reading": "そふがしゅみでしぎんのきょうしつにかよっている。", "example_meaning": "Kakek rutin menghadiri kelas seni tembang puisi shigin sebagai hobinya."},
    {"word": "吟遊", "furigana": "ぎんゆう", "romaji": "ginyuu", "meaning": "Pengelana penyair minstrel keliling", "level": "N1", "example": "中世ヨーロッパの吟遊詩人の物語。", "example_reading": "ちゅうせいよーろっぱのぎんゆうしじんのものがたり。", "example_meaning": "Kisah tentang para penyair pengelana (minstrel) di Eropa abad pertengahan."}
])

add_kanji(11, "銘", "メイ", "", "Merek emiten mengukir prasasti", [
    {"word": "銘柄", "furigana": "めいがら", "romaji": "meigara", "meaning": "Merek dagang / kode saham emiten bursa", "level": "N1", "example": "株式市場で注目されている成長株の銘柄だ。", "example_reading": "かぶしきしじょうでちゅうもくされているせいちょうかぶのめいがらだ。", "example_meaning": "Saham emiten bertumbuh yang tengah menjadi sorotan di pasar bursa."},
    {"word": "感銘", "furigana": "かんめい", "romaji": "kammei", "meaning": "Kesan mendalam terharu kagum membekas", "level": "N1", "example": "恩師の素晴らしい教えに深く感銘を受けた。", "example_reading": "おんしのすばらしいおしえにふかくかんめいをうけた。", "example_meaning": "Menerima kesan yang sangat mendalam atas petuah luar biasa dari sang guru."},
    {"word": "銘記", "furigana": "めいき", "romaji": "meiki", "meaning": "Mematri mengukir dalam ingatan hati", "level": "N1", "example": "教訓をしっかりと心に銘記しておく。", "example_reading": "きょうくんをしっかりとこころにめいきしておく。", "example_meaning": "Mematri pelajaran hidup ini secara kokoh di dalam hati sanubari."}
])

add_kanji(11, "駄", "ダ", "", "Sia-sia mubazir bakiak jajanan", [
    {"word": "無駄", "furigana": "むだ", "romaji": "muda", "meaning": "Sia-sia mubazir buang-buang energi", "level": "N3", "example": "無駄な出費を削って貯金に回す。", "example_reading": "むだなしゅっぴをけずってちょきんにまわす。", "example_meaning": "Memangkas pengeluaran yang sia-sia dan mengalihkannya ke tabungan."},
    {"word": "駄作", "furigana": "ださく", "romaji": "dasaku", "meaning": "Karya buruk gagal mengecewakan", "level": "N1", "example": "評判の割には期待外れの駄作だった。", "example_reading": "ひょうばんのわりにはきたいはづれのださくだった。", "example_meaning": "Meskipun ramai dibicarakan ternyata karya gagal yang mengecewakan."},
    {"word": "駄菓子", "furigana": "だがし", "romaji": "dagashi", "meaning": "Jajanan pasar murah jajanan masa kecil", "level": "N2", "example": "子供の頃に小遣いで駄菓子を買った思い出。", "example_reading": "こどものころにこづかいでだがしをかったおもいで。", "example_meaning": "Kenangan membeli jajanan murah dengan uang saku di masa kecil."}
])

add_kanji(11, "豊", "ホウ", "ゆた・か", "Melimpah ruah makmur kaya", [
    {"word": "豊富", "furigana": "ほうふ", "romaji": "houfu", "meaning": "Melimpah berlimpah ruah banyak ragamnya", "level": "N2", "example": "彼は実務経験が豊富で頼りになる先輩だ。", "example_reading": "かれはじつむけいけんがほうふでたよりになるせんぱいだ。", "example_meaning": "Dia adalah senior yang sangat bisa diandalkan karena kaya akan pengalaman praktik."},
    {"word": "豊作", "furigana": "ほうさく", "romaji": "housaku", "meaning": "Panen raya berlimpah hasil memuaskan", "level": "N2", "example": "秋の実りが豊作で農家の人々が喜んでいる。", "example_reading": "あきのみのりがほうさくでのうかのひとびとがよろこんでいる。", "example_meaning": "Para petani bersukacita karena panen musim gugur berlimpah ruah."}
])

add_kanji(11, "富", "フ、フウ", "と・む、とみ", "Kaya harta melimpah makmur", [
    {"word": "富士山", "furigana": "ふじさん", "romaji": "fujisan", "meaning": "Gunung Fuji (gunung tertinggi di Jepang)", "level": "N4", "example": "新幹線の窓から美しい富士山が見えた。", "example_reading": "しんかんせんのまどからうつくしいふじさんがみえた。", "example_meaning": "Gunung Fuji yang indah terlihat dari jendela kereta Shinkansen."},
    {"word": "富裕", "furigana": "ふゆう", "romaji": "fuyuu", "meaning": "Kekayaan berada kaya raya kemakmuran", "level": "N1", "example": "富裕層をターゲットにした高級住宅街。", "example_reading": "ふゆうそうをたーげっとにしたこうきゅうじゅうたくがい。", "example_meaning": "Kawasan perumahan mewah yang menargetkan kalangan kaya raya."},
    {"word": "富豪", "furigana": "ふごう", "romaji": "fugou", "meaning": "Jutawan konglomerat miliarder", "level": "N1", "example": "一代で巨万の富を築いた大富豪の自伝。", "example_reading": "いちだいできょまんのとみをきずいただいふごうのじでん。", "example_meaning": "Autobiografi konglomerat besar yang membangun kekayaan luar biasa dalam satu generasi."}
])

add_kanji(11, "伐", "バツ", "", "Menebang menumpas menyerang", [
    {"word": "伐採", "furigana": "ばっさい", "romaji": "bassai", "meaning": "Penebangan pohon kayu di hutan", "level": "N1", "example": "森林の過剰な伐採が環境破壊を引き起こす。", "example_reading": "しんりんのかじょうなばっさいがかんきょうはかいをひきおこす。", "example_meaning": "Penebangan hutan yang berlebihan memicu kerusakan lingkungan."},
    {"word": "討伐", "furigana": "とうばつ", "romaji": "toubatsu", "meaning": "Penumpasan penaklukan musuh/pemberontak", "level": "N1", "example": "反乱軍を討伐するために軍隊が派遣された。", "example_reading": "はんらんぐんをとうばつするためにぐんたいがはけんされた。", "example_meaning": "Pasukan militer dikirim untuk menumpas kelompok pemberontak."},
    {"word": "乱伐", "furigana": "らんばつ", "romaji": "rambatsu", "meaning": "Penebangan liar tak terkontrol membabi buta", "level": "N1", "example": "貴重な熱帯雨林の乱伐を国際法で防ぐ。", "example_reading": "きちょうなねったいうりんのらんばつをごくさいほうでふせぐ。", "example_meaning": "Mencegah penebangan liar hutan hujan tropis berharga melalui hukum internasional."}
])

add_kanji(11, "堪", "カン", "た・える", "Mampu menahan, fasih menikmati", [
    {"word": "堪能", "furigana": "たんのう", "romaji": "tannou", "meaning": "Fasih mahir / menikmati sepuasnya", "level": "N1", "example": "フランス語に堪能なスタッフが案内する。", "example_reading": "ふらんすごにたんのうなすたっふがあんないする。", "example_meaning": "Staf yang fasih berbahasa Prancis akan memandu Anda."},
    {"word": "堪忍", "furigana": "かんにん", "romaji": "kannin", "meaning": "Kesabaran pengampunan toleransi", "level": "N1", "example": "これ以上は堪忍袋の緒が切れてしまう。", "example_reading": "これいじょうはかんにんぶくろのおがきれてしまう。", "example_meaning": "Jika lebih dari ini maka batas kesabaran saya akan habis."},
    {"word": "堪え難い", "furigana": "たえがたい", "romaji": "taegatai", "meaning": "Tak tertahankan amat berat ditahan", "level": "N1", "example": "堪え難い痛みに顔をゆがめた。", "example_reading": "たえがたいたみにかおをゆがめた。", "example_meaning": "Meringis kesakitan akibat rasa sakit yang tak tertahankan."}
])

add_kanji(11, "築", "チク", "きず・く", "Membangun mendirikan konstruksi", [
    {"word": "建築", "furigana": "けんちく", "romaji": "kenchiku", "meaning": "Arsitektur konstruksi rancang bangun", "level": "N3", "example": "伝統的な日本の木造建築を研究する。", "example_reading": "でんとうてきなにほんのもくぞうけんちくをけんきゅうする。", "example_meaning": "Meneliti konstruksi arsitektur kayu tradisional Jepang."},
    {"word": "新築", "furigana": "しんちく", "romaji": "shinchiku", "meaning": "Bangunan rumah baru dibangun gres", "level": "N2", "example": "駅の近くに新築のマンションを購入した。", "example_reading": "えきのちかくにしんちくのまんしょんをこうにゅうした。", "example_meaning": "Membeli apartemen baru dibangun di dekat stasiun."},
    {"word": "改築", "furigana": "かいちく", "romaji": "kaichiku", "meaning": "Renovasi pembangunan ulang bangunan", "level": "N1", "example": "古い校舎を全面的に改築する計画だ。", "example_reading": "ふるいこうしゃをぜんめんてきにかいちくするけいかくだ。", "example_meaning": "Rencana untuk merenovasi gedung sekolah tua secara menyeluruh."}
])

add_kanji(11, "崩", "ホウ", "くず・れる、くず・す", "Runtuh ambruk roboh longsor", [
    {"word": "崩壊", "furigana": "ほうかい", "romaji": "houkai", "meaning": "Keruntuhan kehancuran ambruknya sistem", "level": "N1", "example": "バブル経済の崩壊により大不況が訪れた。", "example_reading": "ばぶるけいざいのほうかいによりだいふきょうがおとずれた。", "example_meaning": "Resesi hebat melanda akibat keruntuhan ekonomi gelembung (bubble)."},
    {"word": "崩落", "furigana": "ほうらく", "romaji": "houraku", "meaning": "Longsor runtuhnya tebing bebatuan", "level": "N1", "example": "豪雨で山肌が崩落して道路を塞いだ。", "example_reading": "ごううでやまはだがほうらくしてどうろをふさいだ。", "example_meaning": "Lereng gunung longsor akibat hujan lebat dan menutup akses jalan raya."},
    {"word": "崩御", "furigana": "ほうぎょ", "romaji": "hougyo", "meaning": "Wafat mangkatnya kaisar maharaja", "level": "N1", "example": "天皇陛下の崩御を国民が悼んだ。", "example_reading": "てんのうへいかのほうぎょをごくみんがいたんだ。", "example_meaning": "Rakyat berduka atas mangkatnya Sri Baginda Kaisar."}
])

add_kanji(11, "根", "コン", "ね", "Akar pondasi asal usul dasar", [
    {"word": "根本", "furigana": "こんぽん", "romaji": "kompon", "meaning": "Akar dasar fundamental prinsip pokok", "level": "N2", "example": "問題の根本的な原因を究明する。", "example_reading": "もんだいのこんぽんてきなげんいんをきゅうめいする。", "example_meaning": "Menyelidiki mencari tahu penyebab mendasar dari masalah tersebut."},
    {"word": "根拠", "furigana": "こんきょ", "romaji": "konkyo", "meaning": "Dasar pijakan bukti landasan dalil", "level": "N1", "example": "科学的な根拠に基づいて主張を展開する。", "example_reading": "かがくてきなこんきょにもとづいてしゅちょうをてんかいする。", "example_meaning": "Menyampaikan argumen berlandaskan bukti ilmiah yang kuat."},
    {"word": "屋根", "furigana": "やね", "romaji": "yane", "meaning": "Atap penutup rumah genteng", "level": "N3", "example": "台風で屋根の瓦が吹き飛ばされた。", "example_reading": "たいふうでやねのかわらがふきとばされた。", "example_meaning": "Genteng atap rumah beterbangan tertiup angin topan."}
])

add_kanji(11, "拠", "キョ、コ", "よ・る", "Basis landasan markas bukti", [
    {"word": "拠点", "furigana": "きょてん", "romaji": "kyoten", "meaning": "Basis operasi markas sentra cabang", "level": "N1", "example": "アジア進出の重要な拠点となる支社を設立した。", "example_reading": "あじあしんしゅつのじゅうようなきょてんとなるししゃをせつりつした。", "example_meaning": "Mendirikan kantor cabang yang menjadi basis penting ekspansi ke Asia."},
    {"word": "証拠", "furigana": "しょうこ", "romaji": "shouko", "meaning": "Barang bukti bukti nyata saksi verifikasi", "level": "N2", "example": "警察が犯行の決定的な証拠を押さえた。", "example_reading": "けいさつがはんこうのけっていてきなしょうこをおさえた。", "example_meaning": "Polisi mengamankan barang bukti penentu dari tindak kejahatan."},
    {"word": "根拠", "furigana": "こんきょ", "romaji": "konkyo", "meaning": "Dasar landasan argumen alasan kuat", "level": "N1", "example": "根拠のない噂話を信じてはいけない。", "example_reading": "こんきょのないうわさばなしをしんじてはいけない。", "example_meaning": "Tidak boleh mempercayai kabar burung desas-desus tanpa dasar."}
])

add_kanji(11, "著", "チョ", "あらわ・す、いちじる・しい", "Menulis buku tersohor mencolok", [
    {"word": "著名", "furigana": "ちょめい", "romaji": "chomei", "meaning": "Tersohor termasyhur ternama terkenal", "level": "N1", "example": "世界的に著名な学者による記念講演。", "example_reading": "せかいてきにちょめいながくしゃによるきねんこうえん。", "example_meaning": "Kuliah umum peringatan oleh sarjana akademisi yang tersohor di dunia."},
    {"word": "著書", "furigana": "ちょしょ", "romaji": "chosho", "meaning": "Buku karya tulis karangan buku", "level": "N2", "example": "彼の著書は多くの言語に翻訳されている。", "example_reading": "かれのちょしょはおおくのげんごにほんやくされている。", "example_meaning": "Buku karyanya telah diterjemahkan ke dalam berbagai bahasa."},
    {"word": "顕著", "furigana": "けんちょ", "romaji": "kencho", "meaning": "Mencolok nyata tampak sangat jelas", "level": "N1", "example": "景気の回復傾向が数字に顕著に表れている。", "example_reading": "けいきのかいふくけいこうがすうじにけんちょにあらわれている。", "example_meaning": "Tren pemulihan ekonomi tampak nyata mencolok pada data angka."}
])

add_kanji(11, "総", "ソウ", "", "Total komprehensif terpadu seluruh", [
    {"word": "総合", "furigana": "そうごう", "romaji": "sougou", "meaning": "Komprehensif terpadu gabungan integrasi", "level": "N2", "example": "総合病院で精密検査を受けることになった。", "example_reading": "そうごうびょういんでせいみつけんさをうけることになった。", "example_meaning": "Diputuskan menjalani pemeriksaan menyeluruh di rumah sakit umum terpadu."},
    {"word": "総額", "furigana": "そうがく", "romaji": "sougaku", "meaning": "Jumlah total nominal keseluruhan nilai", "level": "N2", "example": "プロジェクトの総額は五億円に達した。", "example_reading": "ぷろじぇくとのそうがくはごおくえんにたっした。", "example_meaning": "Jumlah total nilai proyek mencapai 500 juta yen."},
    {"word": "総理", "furigana": "そうり", "romaji": "souri", "meaning": "Perdana menteri kepala pemerintahan", "level": "N2", "example": "内閣総理大臣が記者会見を行った。", "example_reading": "ないかくそうりだいじんがきしゃかいけんをおこなった。", "example_meaning": "Perdana Menteri menggelar konferensi pers di hadapan wartawan."}
])

add_kanji(11, "菜", "サイ", "な", "Sayuran lauk lalap", [
    {"word": "野菜", "furigana": "やさい", "romaji": "yasai", "meaning": "Sayur-mayur sayuran segar", "level": "N4", "example": "新鮮な野菜を毎日たくさん食べる。", "example_reading": "しんせんなやさいをまいにちたくさんたべる。", "example_meaning": "Mengonsumsi banyak sayur-mayur segar setiap hari."},
    {"word": "総菜", "furigana": "そうざい", "romaji": "souzai", "meaning": "Lauk-pauk siap saji masakan lauk harian", "level": "N2", "example": "デパ地下で美味しそうな総菜を買って帰る。", "example_reading": "でぱちかでおいしそうなおそうざいをかってかえる。", "example_meaning": "Membeli aneka lauk-pauk siap saji yang lezat di lantai bawah toserba."},
    {"word": "白菜", "furigana": "はくさい", "romaji": "hakusai", "meaning": "Sawi putih sayur kol cina", "level": "N2", "example": "冬の鍋料理に白菜をたっぷり入れる。", "example_reading": "ふゆのなべりょうりにはくさいをたっぷりいれる。", "example_meaning": "Memasukkan sawi putih berlimpah ke dalam hidangan sup panci (nabemono) musim dingin."}
])

add_kanji(11, "再", "サイ、サ", "ふたた・び", "Lagi kembali ulang kedua kali", [
    {"word": "再開", "furigana": "さいかい", "romaji": "saikai", "meaning": "Pembukaan kembali melanjutkan kembali", "level": "N2", "example": "雨が上がって試合が再開された。", "example_reading": "あめがあがってしあいがさいかいされた。", "example_meaning": "Pertandingan dilanjutkan kembali setelah hujan reda."},
    {"word": "再現", "furigana": "さいげん", "romaji": "saigen", "meaning": "Rekonstruksi mewujudkan memperagakan ulang", "level": "N1", "example": "当時の実験を現代の技術で忠実に再現する。", "example_reading": "とうじのじっけんをげんだいのぎじゅつでちゅうじつにさいげんする。", "example_meaning": "Merekonstruksi eksperimen masa lampau secara akurat dengan teknologi modern."},
    {"word": "再生", "furigana": "さいせい", "romaji": "saisei", "meaning": "Pemutaran video daur ulang regenerasi", "level": "N2", "example": "ボタンを押して録音した音声を再生する。", "example_reading": "ぼたんをおしてろくおんしたおんせいをさいせいする。", "example_meaning": "Menekan tombol untuk memutar kembali rekaman suara."}
])

add_kanji(11, "帯", "タイ", "お・びる、おび", "Sabuk sabuk obi zona kawasan", [
    {"word": "地帯", "furigana": "ちたい", "romaji": "chitai", "meaning": "Zona wilayah kawasan sabuk daerah", "level": "N2", "example": "工業地帯に多くの最新工場が集まっている。", "example_reading": "こうぎょうちたいにおおくのさいしんこうじょうがあつまっている。", "example_meaning": "Banyak pabrik modern terpusat di kawasan zona industri."},
    {"word": "熱帯", "furigana": "ねったい", "romaji": "nettai", "meaning": "Iklim tropis wilayah zona tropis", "level": "N2", "example": "熱帯雨林には多種多様な動植物が生息している。", "example_reading": "ねったいうりんにはたしゅたようなどうしょくぶつがせいそくしている。", "example_meaning": "Beraneka ragam flora dan fauna mendiami hutan hujan tropis."},
    {"word": "連帯", "furigana": "れんたい", "romaji": "rentai", "meaning": "Solidaritas kebersamaan ikatan erat", "level": "N1", "example": "労働者たちが固い連帯感を結んで立ち上がった。", "example_reading": "ろうどうしゃたちがかたいれんたいかんをむすんでたちあがった。", "example_meaning": "Para pekerja bangkit bersatu dengan ikatan rasa solidaritas yang kokoh."}
])

add_kanji(11, "救", "キュウ", "すく・う", "Menyelamatkan menolong evakuasi", [
    {"word": "救助", "furigana": "きゅうじょ", "romaji": "kyuujo", "meaning": "Penyelamatan pertolongan evakuasi korban", "level": "N2", "example": "海で溺れかけた少年が救助隊に救助された。", "example_reading": "うみでおぼれかけたしょうねんがきゅうじょたいにきゅうじょされた。", "example_meaning": "Bocah yang nyaris tenggelam di laut berhasil diselamatkan tim evakuasi."},
    {"word": "救援", "furigana": "きゅうえん", "romaji": "kyuuen", "meaning": "Bantuan darurat pasokan bantuan bencana", "level": "N1", "example": "被災地へ救援物資をトラックで輸送する。", "example_reading": "ひさいちへきゅうえんぶっしをとらっくでゆそうする。", "example_meaning": "Mengangkut pasokan logistik bantuan darurat ke lokasi bencana dengan truk."},
    {"word": "救急", "furigana": "きゅうきゅう", "romaji": "kyuukyuu", "meaning": "Gawat darurat ambulans pertolongan pertama", "level": "N3", "example": "急病人のために救急車を呼んだ。", "example_reading": "きゅうびょうにんのためにきゅうきゅうしゃをよんだ。", "example_meaning": "Memanggil mobil ambulans untuk menolong pasien gawat darurat."}
])

add_kanji(11, "粧", "ショウ", "", "Berdandan merias kosmetik", [
    {"word": "化粧", "furigana": "けしょう", "romaji": "keshou", "meaning": "Riasan make up kosmetik berdandan", "level": "N3", "example": "出かける前に鏡の前で化粧をする。", "example_reading": "でかけるまえにかがみのまえでけしょうをする。", "example_meaning": "Merias wajah di depan cermin sebelum bepergian."},
    {"word": "粧束", "furigana": "しょうぞく", "romaji": "shouzoku", "meaning": "Busana pakaian adat tradisional ritual", "level": "N1", "example": "祭りの儀式で神職が白い粧束を身にまとう。", "example_reading": "まつりのぎしきでしんしょくがしろいしょうぞくをみにまとう。", "example_meaning": "Pendeta Shinto mengenakan busana jubah putih ritual dalam upacara festival."}
])

add_kanji(11, "益", "エキ、ヤク", "ま・す", "Keuntungan laba manfaat profit", [
    {"word": "利益", "furigana": "りえき", "romaji": "rieki", "meaning": "Keuntungan laba cuan profit", "level": "N2", "example": "新商品の売れ行きが良く大きな利益が出た。", "example_reading": "しんしょうひんのうれゆきがよくおおきなりえきがでた。", "example_meaning": "Penjualan produk baru sangat laris dan menghasilkan keuntungan besar."},
    {"word": "収益", "furigana": "しゅうえき", "romaji": "shuueki", "meaning": "Pendapatan perolehan revenue penghasilan", "level": "N1", "example": "動画配信による広告収益を増やす。", "example_reading": "どうがはいしんによるこうこくしゅうえきをふやす。", "example_meaning": "Meningkatkan pendapatan hasil iklan dari siaran video."},
    {"word": "有益", "furigana": "ゆうえき", "romaji": "yuueki", "meaning": "Bermanfaat berfaedah berguna berguna", "level": "N2", "example": "セミナーで大変有益な情報を得ることができた。", "example_reading": "せみなーでたいへんゆうえきなじょうほうをえることができた。", "example_meaning": "Bisa memperoleh informasi yang sangat bermanfaat di seminar."}
])

add_kanji(11, "貢", "コウ、ク", "みつ・ぐ", "Kontribusi upeti mempersembahkan", [
    {"word": "貢献", "furigana": "こうけん", "romaji": "kouken", "meaning": "Kontribusi sumbangsih jasa nyata", "level": "N2", "example": "地域社会の発展に大きく貢献した。", "example_reading": "ちいきしゃかいのはってんにおおきくこうけんした。", "example_meaning": "Memberikan kontribusi sumbangsih besar bagi kemajuan masyarakat daerah."},
    {"word": "朝貢", "furigana": "ちょうこう", "romaji": "choukou", "meaning": "Upeti persembahan diplomatik kerajaan kuno", "level": "N1", "example": "古代の王朝に朝貢使節団を派遣した歴史。", "example_reading": "こだいのおうちょうにちょうこうしせつだんをはけんしたれきし。", "example_meaning": "Sejarah pengiriman misi delegasi upeti ke dinasti kekaisaran kuno."}
])

add_kanji(11, "献", "ケン、コン", "ささ・げる", "Menyumbangkan mempersembahkan dedikasi", [
    {"word": "献身", "furigana": "けんしん", "romaji": "kenshin", "meaning": "Pengabdian dedikasi tulus jiwa raga", "level": "N1", "example": "医療従事者の献身的な看護に深く感謝する。", "example_reading": "いりょうじゅうじしゃのけんしんてきなかんごにふかくかんしゃする。", "example_meaning": "Sangat berterima kasih atas dedikasi pengabdian tulus tenaga medis."},
    {"word": "献血", "furigana": "けんけつ", "romaji": "kenketsu", "meaning": "Donor darah sukarela", "level": "N2", "example": "駅前の献血バスで献血に協力した。", "example_reading": "えきまえのけんけつばすでけんけつにきょうりょくした。", "example_meaning": "Berpartisipasi mendonorkan darah di bus donor darah depan stasiun."},
    {"word": "貢献", "furigana": "こうけん", "romaji": "kouken", "meaning": "Kontribusi sumbangsih berfaedah", "level": "N2", "example": "科学の進歩に貢献する研究成果だ。", "example_reading": "かがくのしんぽにこうけんするけんきゅうせいかだ。", "example_meaning": "Hasil temuan riset yang berkontribusi nyata pada kemajuan sains."}
])

add_kanji(11, "判", "ハン、バン", "", "Menilai menghakimi stempel", [
    {"word": "判断", "furigana": "はんだん", "romaji": "handan", "meaning": "Penilaian keputusan pertimbangan", "level": "N3", "example": "冷静な判断力を持って行動することが大切だ。", "example_reading": "れいせいなはんだんりょくをもってこうどうすることがたいせつだ。", "example_meaning": "Penting untuk bertindak dengan daya pertimbangan penilaian yang tenang."},
    {"word": "批判", "furigana": "ひはん", "romaji": "hihan", "meaning": "Kritik kecaman evaluasi tajam", "level": "N2", "example": "根拠のない批判には耳を貸さない。", "example_reading": "こんきょのないひはんにはみみをかさない。", "example_meaning": "Tidak menghiraukan kritik yang tidak berdasar."},
    {"word": "審判", "furigana": "しんばん", "romaji": "shimpan", "meaning": "Wasit pengadil hakim pertandingan", "level": "N2", "example": "サッカーの審判がファウルの笛を吹いた。", "example_reading": "さっかーのしんばんがふぁうるのふえをふいた。", "example_meaning": "Wasit sepak bola meniup peluit tanda terjadinya pelanggaran."}
])

add_kanji(11, "殖", "ショク", "ふ・える、ふ・やす", "Berkembang biak melipatgandakan", [
    {"word": "繁殖", "furigana": "はんしょく", "romaji": "hanshoku", "meaning": "Perkembangbiakan reproduksi fauna flora", "level": "N1", "example": "春は野鳥の繁殖期にあたる。", "example_reading": "はるはやちょうのはんしょくきにあたる。", "example_meaning": "Musim semi adalah masa musim kawin berkembang biak burung liar."},
    {"word": "増殖", "furigana": "ぞうしょく", "romaji": "zoushoku", "meaning": "Penggandaan multiplikasi sel pertambahan cepat", "level": "N1", "example": "がん細胞の急激な増殖を抑える新薬。", "example_reading": "がんさいぼうのきゅうげきなぞうしょくをおさえるしんやく。", "example_meaning": "Obat baru yang menekan penggandaan sel kanker yang cepat."},
    {"word": "利殖", "furigana": "りしょく", "romaji": "rishoku", "meaning": "Pelipatgandaan modal uang investasi harta", "level": "N1", "example": "資産を増やすために株式投資で利殖を図る。", "example_reading": "しさんをふやすためにかぶしきとうしでりしょくをはかる。", "example_meaning": "Mengembangkan melipatgandakan aset melalui investasi saham."}
])

add_kanji(11, "乏", "ボウ", "とぼ・しい", "Kurang langka miskin defisit", [
    {"word": "欠乏", "furigana": "けつぼう", "romaji": "ketsubou", "meaning": "Kekurangan kelangkaan defisit pasokan", "level": "N1", "example": "ビタミンが欠乏すると肌荒れの原因になる。", "example_reading": "びたみんがけつぼうするとはだあれのげんいんになる。", "example_meaning": "Kekurangan vitamin dapat menjadi pemicu kulit kering kasar."},
    {"word": "貧乏", "furigana": "びんぼう", "romaji": "bimbou", "meaning": "Miskin papa serba kekurangan uang", "level": "N3", "example": "貧乏な学生時代を乗り越えて成功した。", "example_reading": "びんぼうながくせいじだいをのりこえてせいこうした。", "example_meaning": "Meraih kesuksesan setelah melewati masa-masa miskin saat kuliah."},
    {"word": "窮乏", "furigana": "きゅうぼう", "romaji": "kyuubou", "meaning": "Kemelaratan hidup serba terjepit sengsara", "level": "N1", "example": "戦争による食糧難で生活が極度に窮乏した。", "example_reading": "せんそうによるしょくりょうなんでせいかつがきょくどにきゅうぼうした。", "example_meaning": "Kehidupan sangat melarat akibat krisis pangan perang."}
])

add_kanji(11, "嘆", "タン", "なげ・く", "Mengeluh meratap menghela napas kagum", [
    {"word": "感嘆", "furigana": "かんたん", "romaji": "kantan", "meaning": "Decak kagum terkesima takjub terpukau", "level": "N1", "example": "名画の圧倒的な美しさに思わず感嘆した。", "example_reading": "めいがのあっとうてきなうつくしさにおもわずかんたんした。", "example_meaning": "Spontan berdecak kagum atas keindahan lukisan mahakarya yang memukau."},
    {"word": "嘆息", "furigana": "たんそく", "romaji": "tansoku", "meaning": "Helaan napas keluh kesah duka pilu", "level": "N1", "example": "思い通りにいかない現実に深いため息と嘆息をもらす。", "example_reading": "おもいどおりにいかないげんじつにふかいためいきとたんそくをもらす。", "example_meaning": "Menghela napas panjang meratapi kenyataan yang tidak berjalan sesuai harapan."},
    {"word": "哀嘆", "furigana": "あいたん", "romaji": "aitan", "meaning": "Ratapan duka kepedihan kesedihan", "level": "N1", "example": "愛する者を失った遺族の哀嘆の声が響く。", "example_reading": "あいするものをうしなったいぞくのあいたんのこえがひびく。", "example_meaning": "Suara ratapan duka keluarga yang kehilangan orang tercinta bergema memilukan."}
])

# ==========================================
# MINGGU 12 (26 Kanji)
# 拝、啓、纂、扱、碑、銘、謹、承、葬、唱、涯、宗、覆、往、恩、恵、縛、隔、驚、凍、貧、挑、童、催、諾、鑑
# ==========================================
add_kanji(12, "拝", "ハイ", "おが・む", "Menyembah melihat dengan hormat sujud", [
    {"word": "拝見", "furigana": "はいけん", "romaji": "haiken", "meaning": "Melihat membaca dengan hormat (kenjougo)", "level": "N3", "example": "送っていただいた資料を拝見しました。", "example_reading": "おくっていただいたしりょうをはいけんしました。", "example_meaning": "Saya telah membaca melihat dokumen berkas yang Anda kirimkan."},
    {"word": "拝啓", "furigana": "はいけい", "romaji": "haikei", "meaning": "Salam hormat pembuka surat resmi", "level": "N2", "example": "手紙の書き出しに「拝啓」と記す。", "example_reading": "てがみのかきだしにはいけいとしるす。", "example_meaning": "Menuliskan kata 'Haikei' (salam hormat) di awal surat."},
    {"word": "礼拝", "furigana": "れいはい", "romaji": "reihai", "meaning": "Ibadah sembahyang kebaktian sujud", "level": "N1", "example": "日曜日には教会で礼拝が行われる。", "example_reading": "にちようびにはきょうかいでれいはいがおこなわれる。", "example_meaning": "Ibadah kebaktian diselenggarakan di gereja pada hari Minggu."}
])

add_kanji(12, "啓", "ケイ", "ひら・く", "Membuka mencerahkan wahyu", [
    {"word": "啓発", "furigana": "けいはつ", "romaji": "keihatsu", "meaning": "Pencerahan penyuluhan penyadaran wawasan", "level": "N1", "example": "市民向けの自己啓発セミナーに参加する。", "example_reading": "しみんむけのじこけいはつせみなーにさんかする。", "example_meaning": "Mengikuti seminar pengembangan diri (self-development) untuk warga."},
    {"word": "啓示", "furigana": "けいじ", "romaji": "keiji", "meaning": "Wahyu petunjuk ilahi wangsit", "level": "N1", "example": "夢の中で神の啓示を受けた預言者。", "example_reading": "ゆめのなかでかみのけいじをうけたよげんしゃ。", "example_meaning": "Nabi yang menerima wahyu petunjuk Tuhan di dalam mimpi."},
    {"word": "拝啓", "furigana": "はいけい", "romaji": "haikei", "meaning": "Salam hormat pembuka surat", "level": "N2", "example": "拝啓、時下ますますご清栄のこととお慶び申し上げます。", "example_reading": "はいけい、じかますますごせいえいのこととおよろこびもうしあげます。", "example_meaning": "Dengan hormat, saya mendoakan agar Anda senantiasa sehat dan sejahtera."}
])

add_kanji(12, "纂", "サン", "", "Mengompilasi menyusun kitab kamus", [
    {"word": "編纂", "furigana": "へんさん", "romaji": "hensan", "meaning": "Kompilasi penyusunan kamus buku sejarah", "level": "N1", "example": "十年以上の歳月をかけて大辞典を編纂した。", "example_reading": "じゅうねんいじょうのさいげつをかけてだいじてんをへんさんした。", "example_meaning": "Menyusun mengompilasi kamus besar selama lebih dari satu dekade."},
    {"word": "編纂物", "furigana": "へんさんぶつ", "romaji": "hensambutsu", "meaning": "Karya literatur hasil kompilasi buku", "level": "N1", "example": "古代の神話や歴史をまとめた編纂物だ。", "example_reading": "こだいのしんわやれきしをまとめたへんさんぶつだ。", "example_meaning": "Karya hasil kompilasi yang merangkum mitologi dan sejarah kuno."}
])

add_kanji(12, "扱", "ソウ", "あつか・う", "Menangani memperlakukan memegang", [
    {"word": "取扱", "furigana": "とりあつかい", "romaji": "toriatsukai", "meaning": "Penanganan operasional petunjuk penanganan", "level": "N2", "example": "精密機械につき取扱注意とラベルに書かれている。", "example_reading": "せいみつきかいにつきとりあつかいちゅういとらべるにかかれている。", "example_meaning": "Tertulis peringatan 'hati-hati dalam penanganan' karena ini mesin presisi."},
    {"word": "扱い", "furigana": "あつかい", "romaji": "atsukai", "meaning": "Perlakuan pelayanan pengayoman", "level": "N2", "example": "子供扱いしないで一人前として接してほしい。", "example_reading": "こどもあつかいしないでいちにんまえとしてせっしてほしい。", "example_meaning": "Tolong jangan perlakukan saya seperti anak kecil, perlakukanlah secara dewasa."}
])

add_kanji(12, "碑", "ヒ", "いしぶみ", "Batu prasasti tugu monumen", [
    {"word": "記念碑", "furigana": "きねんひ", "romaji": "kinenhi", "meaning": "Monumen tugu tugu peringatan prasasti", "level": "N2", "example": "公園の中央に平和を祈念する記念碑が立つ。", "example_reading": "こうえんのちゅうおうにへいわをきねんするきねんひがたつ。", "example_meaning": "Berdiri sebuah tugu monumen peringatan doa perdamaian di tengah taman."},
    {"word": "歌碑", "furigana": "かひ", "romaji": "kahi", "meaning": "Prasasti batu bertuliskan puisi klasik tanka/haiku", "level": "Umum", "example": "松尾芭蕉が句を詠んだ場所に歌碑が残る。", "example_reading": "まつおばしょうがくをよんだばしょにかひがのこる。", "example_meaning": "Prasasti puisi tersisa di tempat Matsuo Basho melantunkan haiku."},
    {"word": "墓碑", "furigana": "ぼひ", "romaji": "bohi", "meaning": "Batu nisan prasasti makam leluhur", "level": "N1", "example": "風化した墓碑の文字を慎重に読み取る。", "example_reading": "ふうかしたぼひのもじをしんちょうによみとる。", "example_meaning": "Membaca tulisan pada prasasti nisan makam yang termakan usia secara teliti."}
])

add_kanji(12, "銘", "メイ", "", "Merek emiten mengukir dalam kalbu", [
    {"word": "感銘", "furigana": "かんめい", "romaji": "kammei", "meaning": "Kesan mendalam rasa kagum terpatri", "level": "N1", "example": "心を揺さぶる名言に深い感銘を受けた。", "example_reading": "こころをゆさぶるめいげんにふかいかんめいをうけた。", "example_meaning": "Menerima kesan sangat mendalam atas kata mutiara yang menggugah hati."},
    {"word": "銘記", "furigana": "めいき", "romaji": "meiki", "meaning": "Mematri mengingat teguh di dalam sanubari", "level": "N1", "example": "失敗から得た教訓を肝に銘記する。", "example_reading": "しっぱいからえたきょうくんをきもにめいきする。", "example_meaning": "Mematri hikmah pelajaran dari kegagalan secara mendalam di hati."},
    {"word": "銘柄", "furigana": "めいがら", "romaji": "meigara", "meaning": "Merek dagang / kode emiten saham", "level": "N1", "example": "有望な新規上場銘柄を調査する。", "example_reading": "ゆうぼうなしんきじょうじょうめいがらをちょうさする。", "example_meaning": "Menyelidiki kode emiten saham baru melantai di bursa yang berprospek cerah."}
])

add_kanji(12, "謹", "キン", "つつし・む", "Dengan hormat takzim rendah hati", [
    {"word": "謹慎", "furigana": "きんしん", "romaji": "kinshin", "meaning": "Skorsing merenungi kesalahan di rumah sanksi", "level": "N1", "example": "不祥事を起こした選手が自宅謹慎の処分を受けた。", "example_reading": "ふしょうじをおこしたせんしゅがじたくきんしんのしょぶんをうけた。", "example_meaning": "Atlet yang tersandung skandal dijatuhi sanksi skorsing isolasi di rumah."},
    {"word": "謹賀", "furigana": "きんが", "romaji": "kinga", "meaning": "Ucapan selamat dengan takzim (e.g. 謹賀新年)", "level": "N1", "example": "「謹賀新年」と書かれた年賀状を送る。", "example_reading": "きんがしんねんとかかれたねんがじょうをおくる。", "example_meaning": "Mengirimkan kartu pos tahun baru bertuliskan 'Selamat Tahun Baru Takzim'."},
    {"word": "謹呈", "furigana": "きんてい", "romaji": "kintei", "meaning": "Mempersembahkan hadiah buku dengan penuh hormat", "level": "N1", "example": "著者がサインとともに本を恩師に謹呈した。", "example_reading": "ちょしゃがさいんとともにほんをおんしにきんていした。", "example_meaning": "Penulis mempersembahkan bukunya beserta tanda tangan kepada sang guru."}
])

add_kanji(12, "承", "ショウ", "うけたまわ・る", "Menerima menyetujui mewarisi", [
    {"word": "承認", "furigana": "しょうにん", "romaji": "shounin", "meaning": "Persetujuan pengesahan akreditasi approval", "level": "N2", "example": "上司の承認を得てから企画を実行に移す。", "example_reading": "じょうしのしょうにんをえてからきかくをじっこうにうつす。", "example_meaning": "Mengeksekusi rencana proyek setelah mendapat persetujuan dari atasan."},
    {"word": "承諾", "furigana": "しょうだく", "romaji": "shoudaku", "meaning": "Kesediaan menyetujui penerimaan tawaran", "level": "N1", "example": "依頼を快く承諾してくれた。", "example_reading": "いらいをこころよくしょうだくしてくれた。", "example_meaning": "Menyetujui dan menyanggupi permohonan permintaan dengan senang hati."},
    {"word": "継承", "furigana": "けいしょう", "romaji": "keishou", "meaning": "Pewarisan suksesi meneruskan warisan tradisi", "level": "N1", "example": "伝統芸能の技を次世代へ確実に継承する。", "example_reading": "でんとうげいのうのわざをつぎせだいへかくじつにけいしょうする。", "example_meaning": "Mewariskan keahlian seni tradisional ke generasi berikutnya secara pasti."}
])

add_kanji(12, "葬", "ソウ", "ほうむ・る", "Memakamkan menguburkan jenazah duka", [
    {"word": "葬式", "furigana": "そうしき", "romaji": "soushiki", "meaning": "Upacara pemakaman prosesi jenazah", "level": "N3", "example": "黒いスーツを着て知人の葬式に参列した。", "example_reading": "くろいすーつをきてちじんのそうしきにさんれつした。", "example_meaning": "Mengenakan jas setelan hitam menghadiri pemakaman kenalan."},
    {"word": "葬儀", "furigana": "そうぎ", "romaji": "sougi", "meaning": "Prosesi upacara duka pemakaman resmi", "level": "N2", "example": "近隣の斎場でしめやかに葬儀が執り行われた。", "example_reading": "きんりんのさいじょうでしめやかにそうぎがとりおこなわれた。", "example_meaning": "Prosesi pemakaman berlangsung dengan khidmat di rumah duka terdekat."},
    {"word": "冠婚葬祭", "furigana": "かんこんそうさい", "romaji": "kankonsousai", "meaning": "Empat upacara siklus hidup adat (dewasa, nikah, wafat, leluhur)", "level": "N1", "example": "冠婚葬祭のマナーを身につけておく。", "example_reading": "かんこんそうさいのまなーをみにつけておく。", "example_meaning": "Mempelajari etika tata krama dalam menghadiri empat upacara adat kehidupan."}
])

add_kanji(12, "唱", "ショウ", "とな・える", "Menyerukan menyanyi bersuara", [
    {"word": "合唱", "furigana": "がっしょう", "romaji": "gasshou", "meaning": "Paduan suara kor nyanyi bersama", "level": "N2", "example": "体育館に美しい合唱の歌声が響き渡る。", "example_reading": "たいいくかんにうつくしいがっしょうのうたごえがひびきわたる。", "example_meaning": "Suara nyanyian paduan suara yang indah menggema di gedung olahraga."},
    {"word": "提唱", "furigana": "ていしょう", "romaji": "teishou", "meaning": "Advokasi mengusulkan terobosan konsep", "level": "N1", "example": "持続可能な都市づくりの構想を提唱する。", "example_reading": "じぞくかのうなまちづくりのこうそうをていしょうする。", "example_meaning": "Mengadvokasikan konsep pembangunan tata kota berkelanjutan."}
])

add_kanji(12, "涯", "ガイ", "", "Ujung batas pantai seumur hidup", [
    {"word": "生涯", "furigana": "しょうがい", "romaji": "shougai", "meaning": "Seumur hidup sepanjang hayat masa hidup", "level": "N2", "example": "彼は生涯を通じて平和運動に身を捧げた。", "example_reading": "かれはしょうがいをつうじてへいわうんどうにみをささげた。", "example_meaning": "Dia mendedikasikan hidupnya sepanjang hayat untuk gerakan perdamaian."},
    {"word": "境涯", "furigana": "きょうがい", "romaji": "kyougai", "meaning": "Kondisi nasib peruntungan jalan hidup", "level": "N1", "example": "数奇な境涯にめげず前を向いて生きる。", "example_reading": "すうきなきょうがいにめげずまえをむいていきる。", "example_meaning": "Tetap menatap maju menjalani hidup tanpa putus asa meski nasib berliku-liku."}
])

add_kanji(12, "宗", "シュウ、ソウ", "", "Agama sekte mazhab leluhur", [
    {"word": "宗教", "furigana": "しゅうきょう", "romaji": "shuukyou", "meaning": "Agama keyakinan iman religi", "level": "N3", "example": "世界の様々な宗教と文化の違いを理解する。", "example_reading": "せかいのさまざまなしゅうきょうとぶんかのちがいをりかいする。", "example_meaning": "Memahami perbedaan aneka ragam agama dan budaya di dunia."},
    {"word": "宗派", "furigana": "しゅうは", "romaji": "shuuha", "meaning": "Aliran sekte mazhab keagamaan", "level": "N1", "example": "仏教には様々な宗派が存在する。", "example_reading": "ぶっきょうにはさまざまなしゅうはがそんざいする。", "example_meaning": "Dalam agama Buddha terdapat berbagai sekte aliran mazhab."},
    {"word": "宗旨", "furigana": "しゅうし", "romaji": "shuushi", "meaning": "Intisari ajaran sekte agama / prinsip hidup", "level": "N1", "example": "我が家の代々の宗旨に従って法要を営む。", "example_reading": "わがいえのだいだいのしゅうしにしたがってほうようをいとなむ。", "example_meaning": "Menyelenggarakan upacara doa arwah sesuai ajaran mazhab turun temurun keluarga."}
])

add_kanji(12, "覆", "フク", "おお・う、くつがえ・す", "Menutupi membalikkan terbalik", [
    {"word": "覆面", "furigana": "ふくめん", "romaji": "fukumen", "meaning": "Topeng penutup muka masker rahasia", "level": "N1", "example": "覆面パトカーがスピード違反を取り締まる。", "example_reading": "ふくめんぱとかーがすぴーどいはんをとりしまる。", "example_meaning": "Mobil patroli polisi tanpa stiker (penyamaran) menindak pelanggar batas kecepatan."},
    {"word": "転覆", "furigana": "てんぷく", "romaji": "tempuku", "meaning": "Terbalik karam kapal / penggulingan kuasa", "level": "N1", "example": "高波を受けて小型漁船が転覆した。", "example_reading": "たかなみをうけてこがたぎょせんがてんぷくした。", "example_meaning": "Perahu nelayan kecil terbalik karam dihantam gelombang tinggi."},
    {"word": "覆水", "furigana": "ふくすい", "romaji": "fukusui", "meaning": "Air tumpah (覆水盆に返らず = nasi sudah jadi bubur)", "level": "N1", "example": "覆水盆に返らず、過去を悔やんでも始まらない。", "example_reading": "ふくすいぼんにかえらず、かこをくやんでもはじまらない。", "example_meaning": "Nasi sudah jadi bubur, menyesali masa lalu tak akan mengubah apa pun."}
])

add_kanji(12, "往", "オウ", "い・く", "Pergi berangkat pulang masa silam", [
    {"word": "往復", "furigana": "おうふく", "romaji": "oufuku", "meaning": "Pulang pergi perjalanan bolak balik tiket PP", "level": "N3", "example": "新幹線の往復チケットを予約した。", "example_reading": "しんかんせんのおうふくちけっとをよやくした。", "example_meaning": "Memesan tiket pulang pergi kereta Shinkansen."},
    {"word": "往来", "furigana": "おうらい", "romaji": "ourai", "meaning": "Lalu lalang hilir mudik orang kendaraan", "level": "N1", "example": "人通りの多い大通りを行き交う車の往来。", "example_reading": "ひとどおりのおおいおおどおりをいきかうくるまのおうらい。", "example_meaning": "Hilir mudik lalu lalang mobil di jalan raya yang ramai pejalan kaki."},
    {"word": "往時", "furigana": "おうじ", "romaji": "ouji", "meaning": "Masa lampau tempo dulu masa silam", "level": "N1", "example": "古写真を見ながら往時の町の姿を偲ぶ。", "example_reading": "こしゃしんをみながらおうじのまちのすがたをしのぶ。", "example_meaning": "Mengenang rupa kota di masa silam sambil memandangi foto kuno."}
])

add_kanji(12, "恩", "オン", "", "Kebaikan budi jasa pertolongan berkah", [
    {"word": "恩恵", "furigana": "おんけい", "romaji": "onkei", "meaning": "Berkah anugerah faedah kebaikan", "level": "N2", "example": "科学技術の発展による恩恵を享受する。", "example_reading": "かがくぎじゅつのはってんによるおんけいをきょうじゅする。", "example_meaning": "Menikmati berkah faedah dari kemajuan ilmu sains dan teknologi."},
    {"word": "恩人", "furigana": "おんじん", "romaji": "onjin", "meaning": "Orang yang sangat berjasa penolong hidup", "level": "N2", "example": "困った時に助けてくれた恩人に会いに行く。", "example_reading": "こまったときにたすけてくれたおんじんにあいにいく。", "example_meaning": "Pergi menemui orang yang sangat berjasa menolong saya di kala susah."},
    {"word": "恩師", "furigana": "おんし", "romaji": "onshi", "meaning": "Guru yang sangat berjasa pendidik tercinta", "level": "N2", "example": "同窓会で高校時代の恩師と再会した。", "example_reading": "どうそうかいでこうこうじだいのおんしとさいかいした。", "example_meaning": "Bertemu kembali dengan guru yang sangat berjasa di masa SMA pada acara reuni."}
])

add_kanji(12, "恵", "ケイ、エ", "めぐ・む、めぐ・み", "Anugerah berkah karunia kecerdikan", [
    {"word": "恩恵", "furigana": "おんけい", "romaji": "onkei", "meaning": "Berkah anugerah faedah rahmat", "level": "N2", "example": "豊かな大自然の恩恵に感謝して暮らす。", "example_reading": "ゆたかなだいしぜんのおんけいにかんしゃしてくらす。", "example_meaning": "Menjalani hidup dengan bersyukur atas berkah anugerah alam yang kaya."},
    {"word": "知恵", "furigana": "ちえ", "romaji": "chie", "meaning": "Kearifan hikmah akal kecerdikan ide cerdas", "level": "N3", "example": "みんなで知恵を出し合って困難を乗り越える。", "example_reading": "みんなでちえをだしあってこんなんをのりこえる。", "example_meaning": "Saling menyumbangkan ide dan kearifan bersama demi mengatasi kesulitan."},
    {"word": "特恵", "furigana": "とっけい", "romaji": "tokkei", "meaning": "Perlakuan preferensial hak istimewa dagang", "level": "N1", "example": "発展途上国に対する特恵関税を適用する。", "example_reading": "はってんとじょうこくにたいするとっけいかんぜいをてきようする。", "example_meaning": "Menerapkan tarif bea cukai preferensial istimewa bagi negara berkembang."}
])

add_kanji(12, "縛", "バク", "しば・る", "Mengikat membelenggu mengekang", [
    {"word": "束縛", "furigana": "そくばく", "romaji": "sokubaku", "meaning": "Pengekangan belenggu ikatan kebebasan", "level": "N1", "example": "ルールに束縛されず自由な発想で挑む。", "example_reading": "るーるにそくばくされずじゆうなはっそうでいどむ。", "example_meaning": "Menantang tanpa terkekang oleh aturan dan menggunakan ide yang bebas."},
    {"word": "捕縛", "furigana": "ほばく", "romaji": "hobaku", "meaning": "Penangkapan pembekukan pencidukan buronan", "level": "N1", "example": "逃走中の指名手配犯が警察に捕縛された。", "example_reading": "とうそうちゅうのしめいてはいはんがけいさつにほばくされた。", "example_meaning": "Buronan yang melarikan diri berhasil dibekuk ditangkap oleh polisi."}
])

add_kanji(12, "隔", "カク", "へだ・たる、へだ・てる", "Memisahkan berjarak interval berselang", [
    {"word": "間隔", "furigana": "かんかく", "romaji": "kankaku", "meaning": "Interval jarak rentang spasi waktu/ruang", "level": "N2", "example": "前の車と十分な車間距離の間隔をあける。", "example_reading": "まえのくるまとじゅうぶんなしゃかんきょりのかんかくをあける。", "example_meaning": "Menjaga jarak interval aman yang cukup dengan mobil di depan."},
    {"word": "隔離", "furigana": "かくり", "romaji": "kakuri", "meaning": "Isolasi karantina pemisahan tempat", "level": "N1", "example": "空港の検疫で感染疑いのある乗客を隔離した。", "example_reading": "くうこうのけんえきでかんせんうたがいのあるじょうきゃくをかくりした。", "example_meaning": "Mengisolasi penumpang yang dicurigai terinfeksi di pos karantina bandara."},
    {"word": "隔週", "furigana": "かくしゅう", "romaji": "kakushuu", "meaning": "Dua minggu sekali berselang sepekan", "level": "N1", "example": "隔週で社内ミーティングが開催される。", "example_reading": "かくしゅうでしゃないみーてぃんぐがかいさいされる。", "example_meaning": "Rapat internal kantor diselenggarakan setiap dua minggu sekali."}
])

add_kanji(12, "驚", "キョウ", "おどろ・く、おどろ・かす", "Terkejut kaget heran takjub", [
    {"word": "驚異", "furigana": "きょうい", "romaji": "kyoui", "meaning": "Keajaiban fenomena mencengangkan luar biasa", "level": "N1", "example": "現代医学の驚異的な進歩に驚かされる。", "example_reading": "げんだいいがくのきょういてきなしんぽにおどろかされる。", "example_meaning": "Dibuat takjub oleh kemajuan ilmu kedokteran modern yang luar biasa mencengangkan."},
    {"word": "驚嘆", "furigana": "きょうたん", "romaji": "kyoutan", "meaning": "Rasa takjub terpukau kagum terheran-heran", "level": "N1", "example": "超絶技巧のピアノ演奏に観客が驚嘆した。", "example_reading": "ちょうぜつぎこうのぴあのえんそうにかんきゃくがきょうたんした。", "example_meaning": "Para penonton terpukau takjub atas kemahiran teknik bermain piano yang luar biasa."},
    {"word": "驚愕", "furigana": "きょうがく", "romaji": "kyougaku", "meaning": "Kaget hebat terperanjat syok gempar", "level": "N1", "example": "予想外の衝撃的なニュースに世界中が驚愕した。", "example_reading": "よそうがいのしょうげきてきなにゅーすにせかいじゅうがきょうがくした。", "example_meaning": "Seluruh dunia terperanjat kaget atas kabar berita mengejutkan yang tak disangka."}
])

add_kanji(12, "凍", "トウ", "こお・る、こご・える", "Beku membeku es", [
    {"word": "冷凍", "furigana": "れいとう", "romaji": "reitou", "meaning": "Pembekuan makanan beku freezer", "level": "N3", "example": "冷凍食品を電子レンジで手軽に温める。", "example_reading": "れいとうしょくひんをでんしれんじでてがるにあたためる。", "example_meaning": "Menghangatkan makanan beku dengan praktis di microwave."},
    {"word": "凍結", "furigana": "とうけつ", "romaji": "touketu", "meaning": "Pembekuan jalan licin / pembekuan aset rekening", "level": "N1", "example": "冬の冷え込みで道路が凍結して滑りやすい。", "example_reading": "ふゆのひえこみでどうろがとうけつしてすべりやすい。", "example_meaning": "Jalan raya membeku licin akibat hawa dingin yang menusuk di musim dingin."},
    {"word": "解凍", "furigana": "かいとう", "romaji": "kaitou", "meaning": "Pencairan makanan beku / mengekstrak file arsip", "level": "N2", "example": "圧縮されたzipファイルを解凍して中身を見る。", "example_reading": "あっしゅくされたじっぷふぁいるをかいとうしてなかみをみる。", "example_meaning": "Mengekstrak berkas zip terkompresi lalu melihat isinya."}
])

add_kanji(12, "貧", "ヒン、ビン", "まず・しい", "Miskin kekurangan darah/uang", [
    {"word": "貧困", "furigana": "ひんこん", "romaji": "hinkon", "meaning": "Kemiskinan melarat kesengsaraan hidup", "level": "N2", "example": "世界の貧困問題を解決するための国際支援。", "example_reading": "せかいのひんこんもんだいをかいけつするためのこくさいしえん。", "example_meaning": "Bantuan internasional untuk memecahkan masalah kemiskinan di dunia."},
    {"word": "貧血", "furigana": "ひんけつ", "romaji": "hinketsu", "meaning": "Anemia kekurangan darah pusing", "level": "N2", "example": "朝礼中に立ちくらみがして貧血で倒れた。", "example_reading": "ちょうれいちゅうにたちくらみがしてひんけつでたおれた。", "example_meaning": "Merasa pusing dan pingsan karena anemia saat upacara apel pagi."},
    {"word": "貧弱", "furigana": "ひんじゃく", "romaji": "hinjaku", "meaning": "Rapuh kurus serba kekurangan minim", "level": "N1", "example": "設備が貧弱で十分な研究ができない。", "example_reading": "せつびがひんじゃくでじゅうぶんなけんきゅうができない。", "example_meaning": "Tidak dapat melakukan penelitian yang memadai karena fasilitas yang serba minim rapuh."}
])

add_kanji(12, "挑", "チョウ", "いど・む", "Menantang mencoba rekor provokasi", [
    {"word": "挑戦", "furigana": "ちょうせん", "romaji": "chousen", "meaning": "Tantangan mencoba menantang rintangan", "level": "N3", "example": "新しい資格試験に果敢に挑戦する。", "example_reading": "あたらしいしかくしけんにかかんにちょうせんする。", "example_meaning": "Dengan berani mencoba menantang ujian kualifikasi baru."},
    {"word": "挑発", "furigana": "ちょうはつ", "romaji": "chouhatsu", "meaning": "Provokasi memancing kemarahan godaan", "level": "N1", "example": "相手の挑発に乗らず冷静に対処した。", "example_reading": "あいてのちょうはつにのらずれいせいにたいしょした。", "example_meaning": "Menghadapi dengan tenang tanpa terpancing oleh provokasi lawan."}
])

add_kanji(12, "童", "ドウ", "わらべ", "Anak-anak bocah dongeng", [
    {"word": "童話", "furigana": "どうわ", "romaji": "douwa", "meaning": "Dongeng cerita anak-anak kisah peri", "level": "N3", "example": "アンデルセンの童話を子供に読み聞かせる。", "example_reading": "あんでるせんのどうわをごどもによみきかせる。", "example_meaning": "Membacakan dongeng karya Andersen kepada anak."},
    {"word": "児童", "furigana": "じどう", "romaji": "jidou", "meaning": "Anak-anak murid usia sekolah dasar", "level": "N2", "example": "児童手当の申請手続きを役所で行う。", "example_reading": "じどうてあてのしんせいてつづきをやくしょでおこなう。", "example_meaning": "Mengurus permohonan tunjangan anak di kantor kelurahan pemda."},
    {"word": "童心", "furigana": "どうしん", "romaji": "doushin", "meaning": "Jiwa kanak-kanak kepolosan hati anak", "level": "N1", "example": "雪だるまを作りながら童心に帰った。", "example_reading": "ゆきだるまをつくりながらどうしんにかえった。", "example_meaning": "Kembali merasakan kepolosan jiwa masa kecil saat membuat boneka salju."}
])

add_kanji(12, "催", "サイ", "もよお・す", "Menyelenggarakan menggelar mendesak", [
    {"word": "開催", "furigana": "かいさい", "romaji": "kaisai", "meaning": "Penyelenggaraan perhelatan event acara", "level": "N2", "example": "来月、国際映画祭が東京で開催される。", "example_reading": "らいげつ、こくさいえいがさいがとうきょうでかいさいされる。", "example_meaning": "Bulan depan, festival film internasional akan diselenggarakan di Tokyo."},
    {"word": "主催", "furigana": "しゅさい", "romaji": "shusai", "meaning": "Penyelenggara tuan rumah pelaksana", "level": "N2", "example": "市が主催する市民マラソン大会に出場する。", "example_reading": "しがしゅさいするしみんまらそんたいかいにしゅつじょうする。", "example_meaning": "Ikut serta dalam lomba lari maraton warga yang diselenggarakan oleh pemerintah kota."},
    {"word": "催促", "furigana": "さいそく", "romaji": "saisoku", "meaning": "Mendesak menagih tenggat waktu", "level": "N2", "example": "レポートの提出を教授から催促された。", "example_reading": "れぽーとのていしゅつをきょうじゅからさいそくされた。", "example_meaning": "Saya ditagih didesak oleh profesor untuk mengumpulkan laporan tugas."}
])

add_kanji(12, "諾", "ダク", "", "Menyetujui menyanggupi mengiyakan", [
    {"word": "承諾", "furigana": "しょうだく", "romaji": "shoudaku", "meaning": "Persetujuan kesediaan menyanggupi", "level": "N1", "example": "契約の条件をお互いに承諾した。", "example_reading": "けいやくのじょうけんをおたがいにしょうだくした。", "example_meaning": "Kedua belah pihak saling menyetujui butir-butir syarat kontrak."},
    {"word": "受諾", "furigana": "じゅだく", "romaji": "judaku", "meaning": "Penerimaan ratifikasi pengesahan deklarasi", "level": "N1", "example": "ポツダム宣言を受諾して終戦を迎えた。", "example_reading": "ぽつだむせんげんをじゅだくしてしゅうせんをむかえた。", "example_meaning": "Menerima Deklarasi Potsdam dan menyambut berakhirnya perang."},
    {"word": "快諾", "furigana": "かいだく", "romaji": "kaidaku", "meaning": "Menyetujui dengan senang hati tanpa ragu", "level": "N1", "example": "講演の依頼を二つ返事で快諾してくれた。", "example_reading": "こうえんのいらいをふたつへんじでかいだくしてくれた。", "example_meaning": "Menyetujui tawaran mengisi ceramah kuliah umum dengan senang hati seketika."}
])

add_kanji(12, "鑑", "カン", "かんが・みる", "Mengapresiasi membedakan teladan stempel", [
    {"word": "鑑賞", "furigana": "かんしょう", "romaji": "kanshou", "meaning": "Apresiasi menikmati karya seni film musik", "level": "N2", "example": "休日に美術館で名画を鑑賞するのが趣味だ。", "example_reading": "きゅうじつにびじゅつかんでめいがをかんしょうするのがしゅみだ。", "example_meaning": "Hobi saya adalah menikmati mengapresiasi lukisan mahakarya di museum saat libur."},
    {"word": "図鑑", "furigana": "ずかん", "romaji": "zukan", "meaning": "Ensiklopedia bergambar buku panduan flora fauna", "level": "N2", "example": "子供に昆虫の生態が載った図鑑をプレゼントした。", "example_reading": "こどもにこんちゅうのせいたいがのったずかんをぷれぜんとした。", "example_meaning": "Menghadiahi anak buku ensiklopedia bergambar tentang kehidupan serangga."},
    {"word": "印鑑", "furigana": "いんかん", "romaji": "inkan", "meaning": "Cap stempel resmi tanda tangan hanko", "level": "N3", "example": "銀行口座の開設に印鑑が必要だ。", "example_reading": "ぎんこうこうざのかいせつにいんかんがひつようだ。", "example_meaning": "Dibutuhkan cap stempel resmi (inkan) untuk membuka rekening bank."}
])

# ==========================================
# MINGGU 13 (17 Kanji)
# 劇、牧、荒、懲、模、酸、掟、耕、滅、棲、餌、奪、謎、築、畠、漁、照
# ==========================================
add_kanji(13, "劇", "ゲキ", "", "Drama teater sandiwara pertunjukan", [
    {"word": "劇場", "furigana": "げきじょう", "romaji": "gekijou", "meaning": "Gedung teater gedung pertunjukan", "level": "N3", "example": "伝統ある歌舞伎座の劇場へ足を運んだ。", "example_reading": "でんとうあるかぶきざのげきじょうへあしをはこんだ。", "example_meaning": "Pergi berkunjung ke gedung teater bersejarah Kabukiza."},
    {"word": "劇団", "furigana": "げきだん", "romaji": "gekidan", "meaning": "Rombongan teater sanggar sandiwara", "level": "N2", "example": "有名な劇団四季の公演チケットを予約した。", "example_reading": "ゆうめいなげきだんしきのこうえんちけっとをよやくした。", "example_meaning": "Memesan tiket pementasan sanggar teater ternama Shiki."},
    {"word": "演劇", "furigana": "えんげき", "romaji": "engeki", "meaning": "Pementasan seni drama sandiwara", "level": "N2", "example": "高校の文化祭で英語劇の演劇を披露した。", "example_reading": "こうこうのぶんかさいでえいごげきのえんげきをひろうした。", "example_meaning": "Menampilkan pementasan drama bahasa Inggris pada festival budaya SMA."}
])

add_kanji(13, "牧", "ボク", "まき", "Gembala ternak padang rumput pastor", [
    {"word": "牧場", "furigana": "ぼくじょう", "romaji": "bokujou", "meaning": "Peternakan padang rumput ranch sapi/kuda", "level": "N3", "example": "北海道の広い牧場で搾りたての牛乳を飲んだ。", "example_reading": "ほっかいどうのひろいぼくじょうでしぼりたてのぎゅうにゅうをのんだ。", "example_meaning": "Meminum susu sapi segar langsung perah di padang peternakan luas di Hokkaido."},
    {"word": "牧師", "furigana": "ぼくし", "romaji": "bokushi", "meaning": "Pendeta pastor gereja kristen protestan", "level": "N1", "example": "教会の牧師から心温まる祝福の言葉をいただく。", "example_reading": "きょうかいのぼくしからこころあたたまるしゅくふくのことばをいただく。", "example_meaning": "Menerima doa restu yang menghangatkan hati dari pendeta gereja."},
    {"word": "遊牧", "furigana": "ゆうぼく", "romaji": "yuuboku", "meaning": "Nomaden penggembalaan berpindah ternak", "level": "N1", "example": "モンゴルの大草原で遊牧生活を営む人々。", "example_reading": "もんごるのだいそうげんでゆうぼくせいかつをいとなむひとびと。", "example_meaning": "Orang-orang yang menjalani hidup nomaden penggembala di padang rumput Mongolia."}
])

add_kanji(13, "荒", "コウ", "あら・い、あ・れる、あ・らす", "Ganas rusak porak-poranda liar", [
    {"word": "荒廃", "furigana": "こうはい", "romaji": "kouhai", "meaning": "Porak-poranda rusak terbengkalai kehancuran", "level": "N1", "example": "長年の戦争によって国土が荒廃してしまった。", "example_reading": "ながねんのせんそうによってこくどがこうはいしてしまった。", "example_meaning": "Tanah air hancur porak-poranda terbengkalai akibat perang bertahun-tahun."},
    {"word": "荒波", "furigana": "あらなみ", "romaji": "aranami", "meaning": "Ombak ganas gelombang badai laut menggelegak", "level": "N1", "example": "日本海の荒波を乗り越えて進む漁船。", "example_reading": "にほんかいのあらなみをのりこえてすすむぎょせん。", "example_meaning": "Kapal nelayan melaju menerjang ombak ganas Laut Jepang."},
    {"word": "荒野", "furigana": "こうや", "romaji": "kouya", "meaning": "Padang belantara gurun liar gersang", "level": "N1", "example": "果てしなく広がる荒野を一人で旅する。", "example_reading": "はてしなくひろがるこうやをひとりでたびする。", "example_meaning": "Menjelajahi padang belantara yang membentang tanpa batas seorang diri."}
])

add_kanji(13, "懲", "チョウ", "こ・りる、こ・らす", "Menghukum memberi jera kapok", [
    {"word": "懲罰", "furigana": "ちょうばつ", "romaji": "choubatsu", "meaning": "Hukuman sanksi pendisiplinan pelanggaran", "level": "N1", "example": "軍紀に違反した兵士に対して懲罰が下された。", "example_reading": "ぐんきにいはんしたへいしにたいしてちょうばつがくだされた。", "example_meaning": "Hukuman sanksi disiplin dijatuhkan kepada tentara yang melanggar kode militer."},
    {"word": "懲役", "furigana": "ちょうえき", "romaji": "choueki", "meaning": "Hukuman kurungan penjara berbobot kerja paksa", "level": "N1", "example": "裁判官は被告人に懲役五年を言い渡した。", "example_reading": "さいばんかんはひこくにんにちょうえきごねんをいいわたした。", "example_meaning": "Hakim memvonis terdakwa dengan hukuman lima tahun penjara."},
    {"word": "懲戒", "furigana": "ちょうかい", "romaji": "choukai", "meaning": "Tindakan disipliner sanksi pemecatan kantor", "level": "N1", "example": "会社の金を横領した社員が懲戒解雇された。", "example_reading": "かいしゃのかねをおうりょうしたしゃいんがちょうかいかいこされた。", "example_meaning": "Karyawan yang menggelapkan uang kantor dipecat secara sanksi disipliner."}
])

add_kanji(13, "模", "モ、ボ", "", "Pola model skala meniru tiruan", [
    {"word": "規模", "furigana": "きぼ", "romaji": "kibo", "meaning": "Skala cakupan ukuran besar dimensi", "level": "N2", "example": "地球規模で環境問題の解決に取り組む。", "example_reading": "ちきゅうきぼでかんきょうもんだいのかいけつにとりくむ。", "example_meaning": "Berupaya mengatasi masalah lingkungan dalam skala global sedunia."},
    {"word": "模倣", "furigana": "もほう", "romaji": "mohou", "meaning": "Peniruan imitasi mencontoh menyontek", "level": "N1", "example": "他人の優れた技術を模倣することから学ぶ。", "example_reading": "たにんのすぐれたぎじゅつをもほうすることからまなぶ。", "example_meaning": "Belajar dengan cara meniru mencontoh teknologi unggul orang lain."},
    {"word": "模範", "furigana": "もはん", "romaji": "mohan", "meaning": "Teladan contoh panutan panutan baik", "level": "N1", "example": "彼は誰からも信頼される模範的なリーダーだ。", "example_reading": "かれはだれからもしんらいされるもはんてきなりーだーだ。", "example_meaning": "Dia adalah sosok pemimpin teladan yang dipercaya oleh siapa pun."}
])

add_kanji(13, "酸", "サン", "す・い", "Asam oksigen korosif asam kimia", [
    {"word": "酸素", "furigana": "さんそ", "romaji": "sanso", "meaning": "Gas oksigen zat asam", "level": "N2", "example": "高山では空気が薄く酸素が不足しやすい。", "example_reading": "こうざんではくうきがうすくさんそがふそくしやすい。", "example_meaning": "Di gunung tinggi udara tipis dan mudah kekurangan oksigen."},
    {"word": "酸化", "furigana": "さんか", "romaji": "sanka", "meaning": "Oksidasi reaksi kimia asam pengaratan", "level": "N1", "example": "鉄が空気中の酸素と反応して酸化する。", "example_reading": "てつがくうきちゅうのさんそとはんのうしてさんかする。", "example_meaning": "Besi teroksidasi bereaksi dengan oksigen di udara."},
    {"word": "炭酸", "furigana": "たんさん", "romaji": "tansan", "meaning": "Asam karbonat minuman bersoda soda", "level": "N2", "example": "暑い夏に冷たい炭酸飲料を一気に飲む。", "example_reading": "あついなつにつめたいたんさんいんりょうをいっきにのむ。", "example_meaning": "Meminum minuman bersoda dingin sekaligus di musim panas yang terik."}
])

add_kanji(13, "掟", "ジョウ", "おきて", "Aturan adat pantangan hukum adat", [
    {"word": "掟", "furigana": "おきて", "romaji": "okite", "meaning": "Aturan adat pantangan leluhur kode etik", "level": "N1", "example": "忍者の世界には厳しい掟が存在した。", "example_reading": "にんじゃのせかいにはきびしいおきてがそんざいした。", "example_meaning": "Dalam dunia ninja terdapat aturan adat pantangan yang sangat keras."},
    {"word": "掟破り", "furigana": "おきてやぶり", "romaji": "okiteyaburi", "meaning": "Pelanggaran aturan adat melanggar tabu", "level": "N1", "example": "常識を覆す掟破りの新戦術で勝利した。", "example_reading": "じょうしきをくつがえすおきてやぶりのしんせんじゅつでしょうりした。", "example_meaning": "Meraih kemenangan dengan taktik baru yang melanggar tabu kebiasaan umum."}
])

add_kanji(13, "耕", "コウ", "たがや・す", "Membajak bercocok tanam membajak sawah", [
    {"word": "耕作", "furigana": "こうさく", "romaji": "kousaku", "meaning": "Penggarapan lahan bercocok tanam pertanian", "level": "N1", "example": "休耕地を耕作して有機野菜を栽培する。", "example_reading": "きゅうこうちをこうさくしてゆうきやさいをさいばいする。", "example_meaning": "Menggarap lahan tidur untuk membudidayakan sayuran organik."},
    {"word": "耕地", "furigana": "こうち", "romaji": "kouchi", "meaning": "Lahan tanah pertanian sawah ladang siap tanam", "level": "N1", "example": "ダム建設によって肥沃な耕地が水没した。", "example_reading": "だむけんせつによってひよくなこうちがすいぼつした。", "example_meaning": "Lahan pertanian yang subur terendam air akibat pembangunan bendungan."},
    {"word": "耕運", "furigana": "こううん", "romaji": "kouun", "meaning": "Pembajakan pengolahan tanah traktor bajak", "level": "Umum", "example": "耕運機を使って畑の土を柔らかく耕す。", "example_reading": "こううんきをつかってはたけのつちをやわらかくたがやす。", "example_meaning": "Menggemburkan tanah ladang menggunakan mesin traktor pembajak."}
])

add_kanji(13, "滅", "メツ", "ほろ・びる、ほろ・ぼす", "Punah musnah binasa hancur", [
    {"word": "絶滅", "furigana": "ぜつめつ", "romaji": "zetsumetsu", "meaning": "Kepunahan punahnya spesies hewan flora", "level": "N2", "example": "絶滅の危機に瀕している希少な野生動物を守る。", "example_reading": "ぜつめつのききにひんしているきしょうなやせいどうぶつをまもる。", "example_meaning": "Melindungi satwa liar langka yang berada di ambang kepunahan."},
    {"word": "消滅", "furigana": "しょうめつ", "romaji": "shoumetsu", "meaning": "Kelenyapan sirna musnah hilang tanpa sisa", "level": "N1", "example": "人口減少により過疎の村が消滅の危機にある。", "example_reading": "じんこうげんしょうによりかそのむらがしょうめつのききにある。", "example_meaning": "Desa terpencil berada dalam ancaman kelenyapan akibat penurunan populasi."},
    {"word": "全滅", "furigana": "ぜんめつ", "romaji": "zemmetsu", "meaning": "Musnah total hancur binasa tanpa sisa", "level": "N1", "example": "害虫の大発生で農作物が全滅した。", "example_reading": "がいちゅうのだいはっせいでのうさくぶつがぜんめつした。", "example_meaning": "Hasil tanaman pertanian musnah total akibat wabah hama serangga."}
])

add_kanji(13, "棲", "セイ", "す・む", "Tinggal berhabitat bermukim", [
    {"word": "同棲", "furigana": "どうせい", "romaji": "dousei", "meaning": "Tinggal serumah hidup bersama tanpa ikatan nikah", "level": "N1", "example": "結婚を前提にアパートで同棲を始めた。", "example_reading": "けっこんをぜんていにあぱーとでどうせいをはじめた。", "example_meaning": "Mulai tinggal serumah bersama di apartemen dengan komitmen menuju pernikahan."},
    {"word": "棲息", "furigana": "せいそく", "romaji": "seisoku", "meaning": "Berhabitat hidup mendiami alam liar", "level": "N1", "example": "深海に棲息する珍しい生物を潜水艇で調査する。", "example_reading": "しんかいにせいそくするめずらしいせいぶつをせんすいていでちょうさする。", "example_meaning": "Menyelidiki makhluk langka yang berhabitat di laut dalam menggunakan kapal selam."}
])

add_kanji(13, "餌", "ジ", "えさ、え", "Umpan mangsa pakan makanan hewan", [
    {"word": "餌", "furigana": "えさ", "romaji": "esa", "meaning": "Pakan makanan hewan / umpan", "level": "N2", "example": "毎朝水槽の金魚に餌をあげる。", "example_reading": "まいあさすいそうのきんぎょにえさをあげる。", "example_meaning": "Memberi makan pakan ikan mas koki di akuarium setiap pagi."},
    {"word": "餌食", "furigana": "えじき", "romaji": "ejiki", "meaning": "Mangsa santapan hewan korban empuk", "level": "N1", "example": "ライオンの餌食となったシマウマ。", "example_reading": "らいおんのえじきとなったしまうま。", "example_meaning": "Zebra yang menjadi mangsa santapan singa pemangsa."},
    {"word": "釣餌", "furigana": "つりえ", "romaji": "tsurie", "meaning": "Umpan pancing ikan", "level": "Umum", "example": "針に釣餌をつけて川に投げ入れた。", "example_reading": "はりにつりえをつけてかわになげいれた。", "example_meaning": "Memasang umpan pancing pada kail lalu melemparkannya ke sungai."}
])

add_kanji(13, "奪", "ダツ", "うば・う", "Merebut merampas mengambil paksa", [
    {"word": "略奪", "furigana": "りゃくだつ", "romaji": "ryakudatsu", "meaning": "Penjarahan perampasan harta benda kekayaan", "level": "N1", "example": "暴動に乗じた商店の略奪を警察が阻止した。", "example_reading": "ぼうどうにじょうじたしょうてんのりゃくだつをけいさつがそしした。", "example_meaning": "Polisi menggagalkan aksi penjarahan toko yang memanfaatkan situasi kerusuhan."},
    {"word": "奪回", "furigana": "だっかい", "romaji": "dakkai", "meaning": "Perebutan kembali mengambil alih posisi", "level": "N1", "example": "敵に占領された要衝を激戦の末に奪回した。", "example_reading": "てきにせんりょうされたようしょうをげきせんのすえにだっかいした。", "example_meaning": "Berhasil merebut kembali posisi penting yang diduduki musuh setelah pertempuran sengit."},
    {"word": "強奪", "furigana": "ごうだつ", "romaji": "goudatsu", "meaning": "Perampokan perampasan dengan kekerasan senjata", "level": "N1", "example": "輸送車から多額の現金を強奪した犯人グループ。", "example_reading": "ゆそうしゃからたがくのげんきんをごうだつしたはんにんぐるーぷ。", "example_meaning": "Kelompok pelaku yang merampas uang tunai dalam jumlah besar dari mobil pengantar."}
])

add_kanji(13, "謎", "メイ", "なぞ", "Teka-teki misteri rahasia tebak", [
    {"word": "謎解き", "furigana": "なぞとき", "romaji": "nazotoki", "meaning": "Pemecahan teka-teki mengungkap misteri", "level": "N2", "example": "脱出ゲームで仲間と謎解きに挑戦する。", "example_reading": "だっしゅつげーむでなかまとなぞときにちょうせんする。", "example_meaning": "Mencoba memecahkan teka-teki bersama teman di permainan escape room."},
    {"word": "謎めく", "furigana": "なぞめく", "romaji": "nazomeku", "meaning": "Bernuansa misterius penuh teka-teki teka-teki", "level": "N1", "example": "謎めいた微笑みを浮かべた絵画の女性。", "example_reading": "なぞめいたほほえみをうかべたかいがのじょせい。", "example_meaning": "Wanita dalam lukisan yang menyunggingkan senyuman penuh misteri."}
])

add_kanji(13, "築", "チク", "きず・く", "Membangun mendirikan rancang susun", [
    {"word": "建築", "furigana": "けんちく", "romaji": "kenchiku", "meaning": "Arsitektur rancang bangun konstruksi", "level": "N3", "example": "世界遺産に登録された歴史的建築物を訪ねる。", "example_reading": "せかいいさんにとうろくされたれきしてきけんちくぶつをおとずねる。", "example_meaning": "Mengunjungi bangunan bersejarah yang terdaftar sebagai warisan dunia."},
    {"word": "構築", "furigana": "こうちく", "romaji": "kouchiku", "meaning": "Penyusunan pembangunan sistem pondasi relasi", "level": "N1", "example": "強固なセキュリティネットワークを構築する。", "example_reading": "きょうこなせきゅりてぃねっとわーくをこうちくする。", "example_meaning": "Membangun jaringan keamanan sistem yang sangat kokoh."},
    {"word": "築港", "furigana": "ちっこう", "romaji": "chikkou", "meaning": "Pembangunan pelabuhan dermaga perairan", "level": "N1", "example": "大型貨物船を受け入れるための築港工事を進める。", "example_reading": "おおがたかもつせんをうけいれるためのちっこうこうじをすすめる。", "example_meaning": "Melanjutkan proyek pembangunan pelabuhan demi menampung kapal kargo berukuran besar."}
])

add_kanji(13, "畠", "", "はたけ", "Ladang kebun palawija tanah garapan", [
    {"word": "田畠", "furigana": "たばたけ", "romaji": "tabatake", "meaning": "Sawah dan ladang pertanian terbentang", "level": "N1", "example": "青々とした田畠が広がるのどかな田園風景。", "example_reading": "あおあおとしたたばたけがひろがるのどかなでんえんふうけい。", "example_meaning": "Pemandangan pedesaan asri tempat sawah dan ladang hijau membentang luas."},
    {"word": "畠", "furigana": "はたけ", "romaji": "hatake", "meaning": "Ladang kebun tanaman sayuran", "level": "N3", "example": "実家の裏の畠でナスやキュウリを収穫した。", "example_reading": "じっかのうらのはたけでなすやきゅうりをしゅうかくした。", "example_meaning": "Memanen terong dan mentimun di kebun belakang rumah orang tua."}
])

add_kanji(13, "漁", "ギョ、リョウ", "あさ・る", "Menangkap ikan nelayan perikanan", [
    {"word": "漁業", "furigana": "ぎょぎょう", "romaji": "gyogyou", "meaning": "Industri perikanan usaha tangkap ikan laut", "level": "N3", "example": "沿岸漁業を支える地域の漁師たち。", "example_reading": "えんがんぎょぎょうをささえるちいきのりょうしたち。", "example_meaning": "Para nelayan daerah yang menopang industri perikanan pesisir."},
    {"word": "漁船", "furigana": "ぎょせん", "romaji": "gyosen", "meaning": "Kapal penangkap ikan perahu nelayan", "level": "N2", "example": "夜明けとともに漁船が一斉に出港した。", "example_reading": "よあけとともにぎょせんがいっせいによっこうした。", "example_meaning": "Perahu-perahu nelayan berlayar serentak bersamaan dengan fajar menyingsing."},
    {"word": "漁港", "furigana": "ぎょこう", "romaji": "gyokou", "meaning": "Pelabuhan pendaratan ikan dermaga nelayan", "level": "N2", "example": "漁港の朝市で獲れたての新鮮な魚を買う。", "example_reading": "ぎょこうのあさいちでとれたてのしんせんなさかなをかう。", "example_meaning": "Membeli ikan segar hasil tangkapan di pasar pagi pelabuhan nelayan."}
])

add_kanji(13, "照", "ショウ", "て・る、て・らす", "Menyinari cahaya membandingkan kontras", [
    {"word": "照明", "furigana": "しょうめい", "romaji": "shoumei", "meaning": "Pencahayaan tata lampu penerangan", "level": "N2", "example": "部屋の間接照明が落ち着いた雰囲気を醸し出す。", "example_reading": "へやのかんせつしょうめいがおちついたふんいきをかもしだす。", "example_meaning": "Pencahayaan lampu temaram di ruangan menciptakan suasana yang menenangkan."},
    {"word": "対照", "furigana": "たいしょう", "romaji": "taishou", "meaning": "Kontras perbandingan mencolok", "level": "N2", "example": "二人の性格は見事な対照をなしている。", "example_reading": "ふたりのせいかくはみごとなたいしょうをなしている。", "example_meaning": "Kepribadian kedua orang itu membentuk kontras perbandingan yang sangat mencolok."},
    {"word": "参照", "furigana": "さんしょう", "romaji": "sanshou", "meaning": "Rujukan referensi melihat acuan silang", "level": "N1", "example": "詳細については添付の資料をご参照ください。", "example_reading": "しょうさいについてはてんぷのしりょうをごさんしょうください。", "example_meaning": "Untuk rincian selengkapnya silakan merujuk pada berkas dokumen terlampir."}
])

# ==========================================
# MINGGU 14 (22 Kanji)
# 随、跡、絶、福、唯、鐘、獲、御、撃、携、就、慮、貢、献、蓄、興、奮、沈、黙、蝶、網、構
# ==========================================
add_kanji(14, "随", "ズイ", "したが・う", "Mengikuti sewaktu-waktu menyertai", [
    {"word": "随時", "furigana": "ずいじ", "romaji": "zuiji", "meaning": "Sewaktu-waktu setiap saat berkala", "level": "N1", "example": "最新情報は公式ホームページで随時更新されます。", "example_reading": "さいしんじょうほうはこうしきほーむぺーじでずいじこうしんされます。", "example_meaning": "Informasi terbaru akan diperbarui setiap saat di situs web resmi."},
    {"word": "追随", "furigana": "ついずい", "romaji": "tsuizui", "meaning": "Mengekor mengikuti di belakang menyaingi", "level": "N1", "example": "競合他社の追随を許さない圧倒的なシェア。", "example_reading": "きょうごうたしゃのついずいをゆるさないあっとうてきなしぇあ。", "example_meaning": "Pangsa pasar dominan yang tak terkejar oleh kompetitor lain."},
    {"word": "随伴", "furigana": "ずいはん", "romaji": "zuihan", "meaning": "Menyertai mengiringi datang bersamaan", "level": "N1", "example": "経済成長に随伴して公害問題が発生した。", "example_reading": "けいざいせいちょうにずいはんしてこうがいもんだいがはっせいした。", "example_meaning": "Masalah pencemaran lingkungan muncul menyertai pertumbuhan ekonomi."}
])

add_kanji(14, "跡", "セキ", "あと", "Jejak peninggalan situs tapak", [
    {"word": "遺跡", "furigana": "いせき", "romaji": "iseki", "meaning": "Situs peninggalan purbakala reruntuhan", "level": "N2", "example": "古代ローマの遺跡をガイドとともに見学する。", "example_reading": "こだいろーまのいせきをごあいどとともにけんがくする。", "example_meaning": "Mengunjungi meninjau situs purbakala Romawi kuno bersama pemandu wisata."},
    {"word": "奇跡", "furigana": "きせき", "romaji": "kiseki", "meaning": "Keajaiban mukjizat luar biasa anugerah", "level": "N2", "example": "奇跡的に九死に一生を得て助かった。", "example_reading": "きせきてきにきゅうしにいっしょうをえてたすかった。", "example_meaning": "Secara mukjizat ajaib berhasil selamat dari maut yang nyaris merenggut nyawa."},
    {"word": "追跡", "furigana": "ついせき", "romaji": "tsuiseki", "meaning": "Pelacakan pengejaran tracking kurir", "level": "N1", "example": "宅配便の追跡番号を入力して配達状況を調べる。", "example_reading": "たくはいびんのついせきばんごうをにゅうりょくしてはいたつじょうきょうをしらべる。", "example_meaning": "Memasukkan nomor resi pelacakan kurir untuk memeriksa status pengantaran paket."}
])

add_kanji(14, "絶", "ゼツ", "た・える、た・やす", "Putus henti mutlak luar biasa", [
    {"word": "絶望", "furigana": "ぜつぼう", "romaji": "zetsubou", "meaning": "Keputusasaan pupus harapan kelam", "level": "N2", "example": "絶望の淵から立ち直り新たな一歩を踏み出す。", "example_reading": "ぜつぼうのふちからたちなおりあらたないっぽをふみだす。", "example_meaning": "Bangkit kembali dari jurang keputusasaan dan melangkah maju."},
    {"word": "絶大", "furigana": "ぜつだい", "romaji": "zetsudai", "meaning": "Luar biasa besar mutlak teramat agung", "level": "N1", "example": "国民から絶大な支持を集めている指導者。", "example_reading": "こくみんからぜつだいなしじをあつめているしどうしゃ。", "example_meaning": "Pemimpin yang mendulang dukungan luar biasa besar dari segenap rakyat."},
    {"word": "絶頂", "furigana": "ぜっちょう", "romaji": "zetchou", "meaning": "Puncak kulminasi titik puncak kejayaan", "level": "N1", "example": "人気絶頂の時期に突然の引退を発表した。", "example_reading": "にんきぜっちょうのじきにとつぜんのいんたいをはっぴょうした。", "example_meaning": "Mengumumkan pensiun mendadak saat berada di puncak masa popularitasnya."}
])

add_kanji(14, "福", "フク", "", "Kebahagiaan berkah sejahtera nasib baik", [
    {"word": "幸福", "furigana": "こうふく", "romaji": "koufuku", "meaning": "Kebahagiaan rasa bahagia sejahtera", "level": "N3", "example": "家族と過ごす平穏な日々に幸福を感じる。", "example_reading": "かぞくとすごすへいおんなひびにかくふくをかんじる。", "example_meaning": "Merasakan kebahagiaan dalam hari-hari tenang bersama keluarga tercinta."},
    {"word": "福祉", "furigana": "ふくし", "romaji": "fukushi", "meaning": "Kesejahteraan sosial jaminan sosial", "level": "N2", "example": "高齢者福祉の充実を目指して政策を進める。", "example_reading": "こうれいしゃふくしのじゅうじつをござしてせいさくをすすめる。", "example_meaning": "Menjalankan kebijakan demi memantapkan kesejahteraan para lansia."},
    {"word": "祝福", "furigana": "しゅくふく", "romaji": "shukufuku", "meaning": "Berkah restu selamat bahagia", "level": "N1", "example": "多くの友人からの祝福に包まれた結婚式。", "example_reading": "おおくのゆうじんからのしゅくふくにつつまれたけっこんしき。", "example_meaning": "Pesta pernikahan yang dilingkupi doa restu penuh berkah dari para sahabat."}
])

add_kanji(14, "唯", "ユイ、イ", "", "Hanya semata satu-satunya", [
    {"word": "唯一", "furigana": "ゆいいつ", "romaji": "yuiitsu", "meaning": "Satu-satunya tiada duanya tunggal", "level": "N2", "example": "これが彼にとって唯一の希望の光だった。", "example_reading": "これがかれにとってゆいいつのきぼうのひかりだった。", "example_meaning": "Inilah satu-satunya seberkas sinar harapan baginya."},
    {"word": "唯物", "furigana": "ゆいぶつ", "romaji": "yuibutsu", "meaning": "Materialisme paham kebendaan fisik", "level": "N1", "example": "唯物史観の立場から歴史の変遷を考察する。", "example_reading": "ゆいぶつしかんのたちばかられきしのへんせんをこうさつする。", "example_meaning": "Mengkaji dinamika sejarah dari sudut pandang paham materialisme historis."},
    {"word": "唯心", "furigana": "ゆいしん", "romaji": "yuishin", "meaning": "Idealisme murni batin spiritualitas", "level": "N1", "example": "唯心論的な世界観を深く掘り下げる哲学。", "example_reading": "ゆいしんろんてきなせかいかんをふかくほりさげるてつがく。", "example_meaning": "Filsafat yang mendalami pandangan dunia berbasis idealisme spiritualitas batin."}
])

add_kanji(14, "鐘", "ショウ", "かね", "Lonceng genta lonceng kuil", [
    {"word": "警鐘", "furigana": "けいしょう", "romaji": "keishou", "meaning": "Lonceng tanda bahaya peringatan waspada", "level": "N1", "example": "地球環境の危機に対して専門家が警鐘を鳴らした。", "example_reading": "ちきゅうかんきょうのききにたいしてせんもんかがけいしょうをならした。", "example_meaning": "Pakar membunyikan lonceng peringatan tanda bahaya atas krisis lingkungan bumi."},
    {"word": "鐘声", "furigana": "しょうせい", "romaji": "shousei", "meaning": "Dentang suara genta lonceng kuil", "level": "N1", "example": "大晦日の夜に百八つの除夜の鐘声を聞く。", "example_reading": "おおみそかのよるにひゃくやっつのじょやのしょうせいをきく。", "example_meaning": "Mendengarkan 108 kali dentangan lonceng kuil pergantian tahun di malam tahun baru."},
    {"word": "晩鐘", "furigana": "ばんしょう", "romaji": "banshou", "meaning": "Dentang lonceng senja hari penutup petang", "level": "N1", "example": "夕暮れの空に響き渡る寺院の晩鐘。", "example_reading": "ゆうぐれのそらにひびきわたるじいんのばんしょう。", "example_meaning": "Dentang lonceng senja kuil menggema merdu di langit temaram petang."}
])

add_kanji(14, "獲", "カク", "え・る", "Meraih memperoleh menangkap mangsa", [
    {"word": "獲得", "furigana": "かくとく", "romaji": "kakutoku", "meaning": "Perolehan meraih medali kemenangan hak", "level": "N2", "example": "オリンピックで金メダルを獲得する夢を叶えた。", "example_reading": "おりんぴっくできんめだるをかくとくするゆめをかなえた。", "example_meaning": "Mewujudkan impian meraih medali emas di ajang olimpiade."},
    {"word": "獲物", "furigana": "えもの", "romaji": "emono", "meaning": "Hewan buruan mangsa tangkapan hasil buru", "level": "N2", "example": "ハンターが山奥で大きな獲物を仕留めた。", "example_reading": "はんたーがやまおくでおおきなえものをしとめた。", "example_meaning": "Pemburu berhasil melumpuhkan hewan buruan besar di pelosok gunung."},
    {"word": "捕獲", "furigana": "ほかく", "romaji": "hokaku", "meaning": "Penangkapan satwa penangkapan hewan liar", "level": "N1", "example": "市街地に現れた野生のイノシシを無事に捕獲した。", "example_reading": "しがいちにあらわれたやせいのいのししをぶじにほかくした。", "example_meaning": "Berhasil menangkap babi hutan liar yang muncul di kawasan permukiman warga."}
])

add_kanji(14, "御", "ギョ、ゴ", "おん、お", "Mengendalikan kontrol kehormatan", [
    {"word": "制御", "furigana": "せいぎょ", "romaji": "seigyo", "meaning": "Pengendalian kontrol sistem komputer mesin", "level": "N1", "example": "コンピューターで自動運転の車体を精密に制御する。", "example_reading": "こんぴゅーたーでじどううんてんのしゃたいをせいみつにせいぎょする。", "example_meaning": "Mengendalikan bodi mobil kemudi otomatis secara presisi dengan komputer."},
    {"word": "防御", "furigana": "ぼうぎょ", "romaji": "bougyo", "meaning": "Pertahanan tameng tangkisan proteksi", "level": "N1", "example": "相手の強烈なアタックを固い防御で防ぎきった。", "example_reading": "あいてのきょうれつなあたっくをかたいぼうぎょでふせぎきった。", "example_meaning": "Menangkis serangan gencar lawan dengan pertahanan yang sangat kokoh."},
    {"word": "御礼", "furigana": "おれい", "romaji": "orei", "meaning": "Ucapan terima kasih bingkisan tanda terima kasih", "level": "N3", "example": "お世話になった方へ御礼の品を贈った。", "example_reading": "おせわになったかたへおれいのしなをおくった。", "example_meaning": "Mengirimkan bingkisan ucapan terima kasih kepada orang yang telah banyak berjasa."}
])

add_kanji(14, "撃", "ゲキ", "う・つ", "Menyerang menembak memukul bentur", [
    {"word": "攻撃", "furigana": "こうげき", "romaji": "kougeki", "meaning": "Penyerangan ofensif serangan agresi", "level": "N2", "example": "サッカーチームが怒涛の攻撃を仕掛ける。", "example_reading": "さっかーちーむがどとうのこうげきをしかける。", "example_meaning": "Tim sepak bola melancarkan serangan ofensif bergelombang yang dahsyat."},
    {"word": "目撃", "furigana": "もくげき", "romaji": "mokugeki", "meaning": "Penyaksian melihat langsung saksi mata", "level": "N2", "example": "事件の決定的な瞬間を目撃した証人。", "example_reading": "じけんのけっていてきなしゅんかんをもくげきしたしょうにん。", "example_meaning": "Saksi mata yang melihat langsung momen penentu insiden kejadian."},
    {"word": "直撃", "furigana": "ちょくげき", "romaji": "chokugeki", "meaning": "Hantaman langsung benturan telak badai", "level": "N1", "example": "大型の台風が列島を直撃して暴風雨をもたらした。", "example_reading": "おおがたのたいふうがれっとうをちょくげきしてぼうふううをもたらした。", "example_meaning": "Angin topan besar menghantam langsung kepulauan dan membawa badai hujan."}
])

add_kanji(14, "携", "ケイ", "たずさ・える、たずさ・わる", "Membawa serta menggandeng jinjing", [
    {"word": "携帯", "furigana": "けいたい", "romaji": "keitai", "meaning": "Telepon genggam ponsel / dibawa serta", "level": "N3", "example": "外出時に携帯電話を忘れて連絡が取れなかった。", "example_reading": "がいしゅつじにけいたいでんわをわすれてれんらくがとれなかった。", "example_meaning": "Tidak bisa dihubungi karena lupa membawa telepon genggam saat bepergian."},
    {"word": "提携", "furigana": "ていけい", "romaji": "teikei", "meaning": "Kemitraan aliansi kerja sama bisnis", "level": "N1", "example": "海外の有力企業と業務提携を結んだ。", "example_reading": "かいがいのゆうりょくきぎょうとぎょうむていけいをむすんだ。", "example_meaning": "Menjalin aliansi kemitraan operasional bersama perusahaan terkemuka luar negeri."},
    {"word": "連携", "furigana": "れんけい", "romaji": "renkei", "meaning": "Koordinasi sinergi kerja sama tim", "level": "N1", "example": "警察と消防が緊密な連携をとって救助活動を行う。", "example_reading": "けいさつとしょうぼうがきんみつなれんけいをとってきゅうじょかつどうをおこなう。", "example_meaning": "Polisi dan pemadam kebakaran berkoordinasi erat dalam operasi penyelamatan."}
])

add_kanji(14, "就", "シュウ", "つ・く", "Mulai menjabat kerja beroperasi", [
    {"word": "就職", "furigana": "しゅうしょく", "romaji": "shuushoku", "meaning": "Mendapatkan pekerjaan masuk ke dunia kerja", "level": "N3", "example": "希望通りの企業への就職が決まり喜ぶ。", "example_reading": "きぼうどおりのきぎょうへのしゅうしょくがきまりよろこぶ。", "example_meaning": "Bersukacita karena dipastikan diterima kerja di perusahaan idaman."},
    {"word": "就任", "furigana": "しゅうにん", "romaji": "shuunin", "meaning": "Pelantikan pengangkatan memangku jabatan", "level": "N2", "example": "新社長の就任パーティーが盛大に開催された。", "example_reading": "しんしゃちょうのしゅうにんぱーてぃーがせいだいにかいさいされた。", "example_meaning": "Pesta pelantikan direktur utama baru digelar dengan sangat meriah."},
    {"word": "就航", "furigana": "しゅうこう", "romaji": "shuukou", "meaning": "Pelayaran penerbangan perdana beroperasi", "level": "N1", "example": "新しい航路に最新鋭の大型客船が就航した。", "example_reading": "あたらしいこうろにさいしんえいのおおがたきゃくせんがしゅうこうした。", "example_meaning": "Kapal pesiar besar mutakhir mulai beroperasi di rute jalur baru."}
])

add_kanji(14, "慮", "リョ", "おもんぱか・る", "Pertimbangan pemikiran cermat empati", [
    {"word": "考慮", "furigana": "こうりょ", "romaji": "kouryo", "meaning": "Pertimbangan cermat memperhitungkan kondisi", "level": "N2", "example": "諸般の事情を考慮した上で最終的な判断を下す。", "example_reading": "しょはんのじじょうをこうりょしたうえでさいしゅうてきなはんだんをくだす。", "example_meaning": "Mengambil keputusan akhir setelah mempertimbangkan aneka kondisi keadaan."},
    {"word": "配慮", "furigana": "はいりょ", "romaji": "hairyo", "meaning": "Perhatian kepedulian tenggang rasa empati", "level": "N2", "example": "車椅子の方への細やかな配慮が行き届いた施設だ。", "example_reading": "くるまいすのかたへのこまやかなはいりょがいきとどいたしせつだ。", "example_meaning": "Fasilitas yang memiliki kepedulian empati menyeluruh bagi pengguna kursi roda."},
    {"word": "遠慮", "furigana": "えんりょ", "romaji": "enryo", "meaning": "Sungkan menahan diri segan", "level": "N3", "example": "遠慮せずに何でも自由に質問してください。", "example_reading": "えんりょせずになんでもじゆうにしつもんしてください。", "example_meaning": "Silakan bertanya apa saja dengan bebas jangan sungkan-sungkan."}
])

add_kanji(14, "貢", "コウ", "みつ・ぐ", "Kontribusi sumbangsih upeti", [
    {"word": "貢献", "furigana": "こうけん", "romaji": "kouken", "meaning": "Kontribusi sumbangsih jasa berharga", "level": "N2", "example": "新薬の開発によって人類の健康に大きく貢献する。", "example_reading": "しんやくのかいはつによってじんるいのけんこうにおおきくこうけんする。", "example_meaning": "Memberi kontribusi besar bagi kesehatan umat manusia melalui pengembangan obat baru."},
    {"word": "貢物", "furigana": "みつぎもの", "romaji": "mitsugimono", "meaning": "Upeti persembahan tanda ketundukan raja", "level": "N1", "example": "属国から王宮へ貴重な貢物が届けられた。", "example_reading": "ぞっこくからおうきゅうへきちょうなみつぎものがとどけられた。", "example_meaning": "Upeti berharga diantarkan dari negara vasal ke istana kerajaan."}
])

add_kanji(14, "献", "ケン", "ささ・げる", "Pengabdian dedikasi literatur", [
    {"word": "献身", "furigana": "けんしん", "romaji": "kenshin", "meaning": "Pengabdian dedikasi tulus jiwa raga", "level": "N1", "example": "地域医療に生涯を捧げた医師の献身的な活動。", "example_reading": "ちいきいりょうにしょうがいをささげたいしのけんしんてきなかつどう。", "example_meaning": "Aktivitas dedikasi tulus dari dokter yang mendedikasikan hidupnya untuk medis daerah."},
    {"word": "文献", "furigana": "ぶんけん", "romaji": "bunken", "meaning": "Literatur kepustakaan rujukan ilmiah dokumen", "level": "N1", "example": "大学図書館で関連する学術文献を徹底的に調査する。", "example_reading": "だいがくとしょかんでかんれんするがくじゅつぶんけんをてっていてきにちょうさする。", "example_meaning": "Meneliti literatur akademis terkait secara menyeluruh di perpustakaan universitas."},
    {"word": "献立", "furigana": "こんだて", "romaji": "kondate", "meaning": "Susunan menu hidangan masakan resep", "level": "N2", "example": "栄養バランスを考えながら今晩の夕食の献立を決める。", "example_reading": "えいようばらんすをかんがえながらこんばんのゆうしょくのこんだてをきめる。", "example_meaning": "Menentukan susunan menu makan malam dengan mempertimbangkan keseimbangan gizi."}
])

add_kanji(14, "蓄", "チク", "たくわ・える", "Menimbun menyimpan cadangan baterai", [
    {"word": "蓄積", "furigana": "ちくせき", "romaji": "chikuseki", "meaning": "Akumulasi penumpukan simpanan pengalaman", "level": "N1", "example": "長年の研究データの蓄積が新発見をもたらした。", "example_reading": "ながねんのけんきゅうでーたのちくせきがしんはっけんをもたらした。", "example_meaning": "Akumulasi data riset bertahun-tahun membuahkan penemuan baru."},
    {"word": "貯蓄", "furigana": "ちょちく", "romaji": "chochiku", "meaning": "Tabungan simpanan dana simpanan", "level": "N2", "example": "給料の一部を毎月定期的に貯蓄に回す。", "example_reading": "きゅうりょうのいちぶをまいつきていきてきにちょちくにまわす。", "example_meaning": "Menyisihkan sebagian gaji secara rutin setiap bulan ke dalam tabungan."},
    {"word": "蓄電", "furigana": "ちくでん", "romaji": "chikuden", "meaning": "Penyimpanan daya listrik baterai akumulasi", "level": "N1", "example": "大容量の蓄電システムを工場に導入した。", "example_reading": "だいようりょうのちくでんしすてむをこうじょうにどうにゅうした。", "example_meaning": "Mendatangkan sistem penyimpanan daya baterai berkapasitas besar ke pabrik."}
])

add_kanji(14, "興", "コウ、キョウ", "おこ・る、おこ・す", "Minat kebangkitan gairah kegembiraan", [
    {"word": "興味", "furigana": "きょうみ", "romaji": "kyoumi", "meaning": "Minat ketertarikan rasa ingin tahu", "level": "N3", "example": "日本のアニメや伝統文化に深い興味がある。", "example_reading": "にほんのあにめやでんとうぶんかにふかいきょうみがある。", "example_meaning": "Memiliki ketertarikan minat yang mendalam terhadap anime dan budaya tradisional Jepang."},
    {"word": "復興", "furigana": "ふっこう", "romaji": "fukkou", "meaning": "Rekonstruksi kebangkitan pemulihan pasca bencana", "level": "N1", "example": "震災からの復興に向けて街の再建が進んでいる。", "example_reading": "しんさいからのふっこうにむけてまちのさいけんがすすんでいる。", "example_meaning": "Pembangunan kembali kota bergerak maju demi rekonstruksi pemulihan pasca gempa."},
    {"word": "振興", "furigana": "しんこう", "romaji": "shinkou", "meaning": "Pemajuan revitalisasi kemajuan industri/seni", "level": "N1", "example": "観光振興のために新しいイベントを企画する。", "example_reading": "かんこうしんこうのためにあたらしいいべんとをきかくする。", "example_meaning": "Merencanakan acara baru demi memajukan pariwisata daerah."}
])

add_kanji(14, "奮", "フン", "ふる・う", "Semangat berkobar gigih berjuang", [
    {"word": "興奮", "furigana": "こうふん", "romaji": "koufun", "meaning": "Gairah kegembiraan meluap antusiasme tinggi", "level": "N2", "example": "大好きなバンドのライブを見て興奮が冷めない。", "example_reading": "だいすきなばんどのらいぶをみてこうふんがさめない。", "example_meaning": "Antusiasme kegembiraan belum juga reda setelah menonton konser band favorit."},
    {"word": "奮闘", "furigana": "ふんとう", "romaji": "funtou", "meaning": "Perjuangan gigih kerja keras membanting tulang", "level": "N1", "example": "新入社員たちが業務改善に向けて奮闘している。", "example_reading": "しんにゅうしゃいんたちがぎょうむかいぜんにむけてふんとうしている。", "example_meaning": "Karyawan baru berjuang gigih bekerja keras demi perbaikan proses kerja."},
    {"word": "奮起", "furigana": "ふんき", "romaji": "funki", "meaning": "Bangkit bersemangat membulatkan tekad", "level": "N1", "example": "敗北の悔しさをバネに奮起して次の大会に挑む。", "example_reading": "はいぼくのくやしさをばねにふんきしてつぎのたいかいにいどむ。", "example_meaning": "Bangkit membulatkan semangat dari kekecewaan kekalahan untuk menantang turnamen berikutnya."}
])

add_kanji(14, "沈", "チン", "しず・む、しず・める", "Tenggelam karam hening tenang", [
    {"word": "沈没", "furigana": "ちんぼつ", "romaji": "chimbotsu", "meaning": "Tenggelam karamnya kapal karam di laut", "level": "N1", "example": "海底に眠る沈没船から財宝が引き揚げられた。", "example_reading": "かいていにねむるちんぼつせんからざいほうがひきあげられた。", "example_meaning": "Harta karun berhasil diangkat dari kapal karam yang terkubur di dasar laut."},
    {"word": "沈黙", "furigana": "ちんもく", "romaji": "chimmoku", "meaning": "Keheningan hening bungkam seribu bahasa", "level": "N2", "example": "会議室に気まずい沈黙が流れた。", "example_reading": "かいぎしつにきまずいちんもくがながれた。", "example_meaning": "Keheningan canggung yang kaku menyelimuti ruang rapat."},
    {"word": "沈着", "furigana": "ちんちゃく", "romaji": "chinchaku", "meaning": "Tenang berkepala dingin tidak panik (冷静沈着)", "level": "N1", "example": "緊急事態にも沈着に対処する優秀な機長だ。", "example_reading": "きんきゅうじたいにもちんちゃくにたいしょするゆうしゅうなきちょうだ。", "example_meaning": "Kapten pilot andal yang menangani situasi darurat dengan tenang dan berkepala dingin."}
])

add_kanji(14, "黙", "モク", "だま・る", "Diam hening bungkam bisu", [
    {"word": "沈黙", "furigana": "ちんもく", "romaji": "chimmoku", "meaning": "Keheningan hening bungkam tanpa kata", "level": "N2", "example": "長い沈黙を破って彼が口を開いた。", "example_reading": "ながいちんもくをやぶってかれがくちをひらいた。", "example_meaning": "Dia akhirnya buka suara memecah keheningan yang panjang."},
    {"word": "黙秘", "furigana": "もくひ", "romaji": "mokuhi", "meaning": "Hak bungkam tutup mulut dalam pemeriksaan", "level": "N1", "example": "取り調べに対して黙秘権を行使した。", "example_reading": "とりしらべにたいしてもくひけんをこうしした。", "example_meaning": "Menggunakan hak bungkam tutup mulut saat menjalani pemeriksaan penyidikan."},
    {"word": "黙認", "furigana": "もくにん", "romaji": "mokunin", "meaning": "Pembiaran merestui diam-diam tutup mata", "level": "N1", "example": "会社側が違法な残業を黙認していたと指摘された。", "example_reading": "かいしゃがわがいほうなざんぎょうをもくにんしていたとしてきされた。", "example_meaning": "Pihak manajemen dikritik karena membiarkan tutup mata terhadap lembur ilegal."}
])

add_kanji(14, "蝶", "チョウ", "", "Kupu-kupu indah bersayap", [
    {"word": "蝶々", "furigana": "ちょうちょう", "romaji": "chouchou", "meaning": "Kupu-kupu bersayap indah", "level": "N3", "example": "春の野原を色鮮やかな蝶々が舞っている。", "example_reading": "はるのはらをいろあざやかなちょうちょうがまっている。", "example_meaning": "Kupu-kupu berwarna-warni cerah beterbangan menari di padang rumput musim semi."},
    {"word": "蝶結び", "furigana": "ちょうむすび", "romaji": "choumusubi", "meaning": "Simpul pita kupu-kupu ikatan pita", "level": "Umum", "example": "プレゼントの箱にきれいなリボンで蝶結びをする。", "example_reading": "ぷれぜんとのはこにきれいなりぼんでちょうむすびをする。", "example_meaning": "Mengikat simpul pita kupu-kupu yang cantik pada kotak kado hadiah."},
    {"word": "胡蝶", "furigana": "こちょう", "romaji": "kochou", "meaning": "Kupu-kupu dalam sastra (胡蝶の夢)", "level": "N1", "example": "胡蝶の夢という荘子の有名な寓話。", "example_reading": "こちょうのゆめというそうじのゆうめいなぐうわ。", "example_meaning": "Fabel terkenal karya Zhuangzi tentang mimpi sang kupu-kupu (Kochou no Yume)."}
])

add_kanji(14, "網", "モウ", "あみ", "Jaring jala jala-jala transmisi", [
    {"word": "網羅", "furigana": "もうら", "romaji": "moura", "meaning": "Pencakupan menyeluruh memuat komprehensif", "level": "N1", "example": "最新のIT用語を網羅した実用的な辞典だ。", "example_reading": "さいしんのあいてぃーようごをもうらしたじつようてきなじてんだ。", "example_meaning": "Kamus praktis yang mencakup secara komprehensif seluruh istilah IT terkini."},
    {"word": "通信網", "furigana": "つうしんもう", "romaji": "tsuushinmou", "meaning": "Jaringan telekomunikasi transmisi data", "level": "N1", "example": "全国を結ぶ高速通信網が整備された。", "example_reading": "ぜんこくをむすぶこうそくつうしんもうがせいびされた。", "example_meaning": "Jaringan telekomunikasi berkecepatan tinggi yang menghubungkan seantero negeri telah siap."},
    {"word": "魚網", "furigana": "ぎょもう", "romaji": "gyomou", "meaning": "Jaring ikan pukat nelayan jala", "level": "Umum", "example": "港で漁師たちが破れた魚網を丁寧に繕っている。", "example_reading": "みなとでりょうしたちがやぶれたぎょもうをていねいにつくろっている。", "example_meaning": "Para nelayan di pelabuhan merajut memperbaiki jaring ikan yang robek dengan teliti."}
])

add_kanji(14, "構", "コウ", "かま・える、かま・う", "Struktur menyusun merancang peduli", [
    {"word": "構造", "furigana": "こうぞう", "romaji": "kouzou", "meaning": "Struktur susunan kerangka arsitektur", "level": "N2", "example": "地震に強い免震構造のビルを建設する。", "example_reading": "じしんにつよいめんしんこうぞうのびるをけんせつする。", "example_meaning": "Membangun gedung berstruktur tahan gempa isolasi seismik yang kokoh."},
    {"word": "構成", "furigana": "こうせい", "romaji": "kousei", "meaning": "Komposisi susunan formasi anggota", "level": "N2", "example": "論文の全体の構成を論理的に組み立てる。", "example_reading": "ろんぶんのぜんたいのこうせいをろんりてきにくみたてる。", "example_meaning": "Menyusun komposisi keseluruhan naskah skripsi ilmiah secara logis."},
    {"word": "構想", "furigana": "こうそう", "romaji": "kousou", "meaning": "Gagasan konsep visi rancangan masa depan", "level": "N1", "example": "未来都市の壮大な構想を発表した。", "example_reading": "みらいとしのそうだいなこうそうをはっぴょうした。", "example_meaning": "Mengumumkan visi rancangan konsep megah mengenai kota masa depan."}
])

# Combine Existing + New
ALL_DATA = EXISTING_DATA + NEW_DATA

print(f"Existing kanji: {len(EXISTING_DATA)}")
print(f"New kanji added: {len(NEW_DATA)}")
print(f"Total kanji: {len(ALL_DATA)}")

weeks = {}
total_jukugo = 0
for k in ALL_DATA:
    w = k["week"]
    weeks[w] = weeks.get(w, 0) + 1
    total_jukugo += len(k["jukugo"])

print(f"Weeks summary: {sorted(weeks.items())}")
print(f"Total Jukugo: {total_jukugo}")

# Export to data.js
js_content = f"// Dataset Jukugo Master\n// Diperbarui dengan Minggu 1-6 dan Minggu 9-14\n\nconst JUKUGO_DATABASE = {json.dumps(ALL_DATA, ensure_ascii=False, indent=2)};\n\nif (typeof module !== 'undefined' && module.exports) {{\n  module.exports = JUKUGO_DATABASE;\n}}\n"

with open("C:/Users/Pujo Lestariono/.gemini/antigravity/scratch/jukugo-master/data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("data.js successfully updated with all weeks!")
