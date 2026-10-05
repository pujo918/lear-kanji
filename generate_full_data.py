# -*- coding: utf-8 -*-
"""
Script to build full dataset for Jukugo Master.
All kanji from Week 1 to Week 6, strictly between 2 to 4 high-frequency jukugo per kanji.
"""
import json

DATA = []

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
    DATA.append(item)

# ==========================================
# MINGGU 1 (22 Kanji)
# 株、随、勘、佃、熟、錯、誤、極、範、忍、看、蠅、葵、倫、敦、情、息、影、響、愉、快、素
# ==========================================
add_kanji(1, "株", "シュ", "かぶ", "Saham, tunggul tanaman", [
    {"word": "株式", "furigana": "かぶしき", "romaji": "kabushiki", "meaning": "Saham / efek kepemilikan saham", "level": "N2", "example": "彼は株式会社を立ち上げた。", "example_reading": "かれはかぶしきがいしゃをたちあげた。", "example_meaning": "Dia mendirikan perseroan terbatas (PT)."},
    {"word": "株価", "furigana": "かぶか", "romaji": "kabuka", "meaning": "Harga saham", "level": "N2", "example": "株価が大幅に上昇した。", "example_reading": "かぶかがおおはばにじょうしょうした。", "example_meaning": "Harga saham naik drastis."},
    {"word": "株主", "furigana": "かぶぬし", "romaji": "kabunushi", "meaning": "Pemegang saham", "level": "N2", "example": "来週、株主総会が開かれる。", "example_reading": "らいしゅう、かぶぬしそうかいがひらかれる。", "example_meaning": "Rapat umum pemegang saham diadakan minggu depan."}
])

add_kanji(1, "随", "ズイ", "したが・う", "Mengikuti, sesuka hati, sewaktu-waktu", [
    {"word": "随時", "furigana": "ずいじ", "romaji": "zuiji", "meaning": "Sewaktu-waktu / setiap saat / berkala", "level": "N1", "example": "質問は随時受け付けています。", "example_reading": "しつもんはずいじうけつけています。", "example_meaning": "Pertanyaan diterima setiap saat."},
    {"word": "随分", "furigana": "ずいぶん", "romaji": "zuibun", "meaning": "Sangat / lumayan banyak / luar biasa", "level": "N3", "example": "日本語が随分上手になった。", "example_reading": "にほんごがずいぶんじょうずになった。", "example_meaning": "Bahasa Jepangmu sudah sangat meningkat."},
    {"word": "追随", "furigana": "ついずい", "romaji": "tsuizui", "meaning": "Mengekor / mengikuti di belakang", "level": "N1", "example": "他社の追随を許さない技術だ。", "example_reading": "たしゃのついずいをゆるさないぎじゅつだ。", "example_meaning": "Teknologi yang tidak bisa disaingi perusahaan lain."},
    {"word": "随筆", "furigana": "ずいひつ", "romaji": "zuihitsu", "meaning": "Esai / tulisan lepas santai", "level": "N1", "example": "暇な時に随筆を書いている。", "example_reading": "ひまなときにずいひつをかいている。", "example_meaning": "Saya menulis esai santai di waktu luang."}
])

add_kanji(1, "勘", "カン", "", "Intuisi, firasat, perhitungan", [
    {"word": "勘定", "furigana": "かんじょう", "romaji": "kanjou", "meaning": "Perhitungan / bayar tagihan kasir", "level": "N3", "example": "お勘定をお願いします。", "example_reading": "おかんじょうをおねがいします。", "example_meaning": "Tolong minta bon tagihannya."},
    {"word": "勘違い", "furigana": "かんちがい", "romaji": "kanchigai", "meaning": "Salah paham / keliru perkiraan", "level": "N3", "example": "集合時間を勘違いしていた。", "example_reading": "しゅうごうじかんをかんちがいしていた。", "example_meaning": "Saya salah mengira jam kumpul."},
    {"word": "直勘", "furigana": "ちょっかん", "romaji": "chokkan", "meaning": "Firasat langsung / intuisi tajam", "level": "N1", "example": "直勘を信じて決断した。", "example_reading": "ちょっかんをしんじてけつだんした。", "example_meaning": "Saya memutuskan dengan mempercayai intuisi saya."},
    {"word": "勘弁", "furigana": "かんべん", "romaji": "kamben", "meaning": "Memaafkan / ampun / tolerir", "level": "N2", "example": "無理な注文は勘弁してほしい。", "example_reading": "むりなちゅうもんはかんべんしてほしい。", "example_meaning": "Tolong ampuni, jangan minta pesanan yang mustahil."}
])

add_kanji(1, "佃", "デン、テン", "つくだ", "Sawah garapan, tsukuda", [
    {"word": "佃煮", "furigana": "つくだに", "romaji": "tsukudani", "meaning": "Tsukudani (lauk rebusan kecap manis asin khas Jepang)", "level": "Umum", "example": "佃煮をおにぎりの具にする。", "example_reading": "つくだにをおにぎりのぐにする。", "example_meaning": "Menggunakan tsukudani sebagai isian onigiri."},
    {"word": "佃農", "furigana": "でんのう", "romaji": "dennou", "meaning": "Petani penyewa sawah / penggarap lahan", "level": "N1", "example": "歴史の授業で佃農の生活を学んだ。", "example_reading": "れきしのじゅぎょうででんのうのせいかつをまなんだ。", "example_meaning": "Belajar mengenai kehidupan petani penggarap di kelas sejarah."}
])

add_kanji(1, "熟", "ジュク", "う・れる", "Matang, terampil, mendalam", [
    {"word": "熟語", "furigana": "じゅくご", "romaji": "jukugo", "meaning": "Kata majemuk kanji / idiom jukugo", "level": "N2", "example": "新しい熟語をノートにメモした。", "example_reading": "あたらしいじゅくごをのーとにめもした。", "example_meaning": "Mencatat jukugo baru ke dalam buku catatan."},
    {"word": "成熟", "furigana": "せいじゅく", "romaji": "seijuku", "meaning": "Kematangan / kedewasaan", "level": "N1", "example": "果物が成熟して甘くなった。", "example_reading": "くだものがせいじゅくしてあまくなった。", "example_meaning": "Buahnya sudah matang dan menjadi manis."},
    {"word": "熟睡", "furigana": "じゅくすい", "romaji": "jukusui", "meaning": "Tidur nyenyak / tidur pulas", "level": "N2", "example": "疲れていたので朝まで熟睡した。", "example_reading": "つかれていたのであさまでじゅくすいした。", "example_meaning": "Karena lelah, saya tidur pulas sampai pagi."},
    {"word": "未熟", "furigana": "みじゅく", "romaji": "mijuku", "meaning": "Belum matang / mentah / belum berpengalaman", "level": "N2", "example": "未熟な点が多いですが、努力します。", "example_reading": "みじゅくなてんがおおいですが、どりょくします。", "example_meaning": "Masih banyak kekurangan yang belum matang, tapi saya akan berusaha."}
])

add_kanji(1, "錯", "サク", "", "Bercampur aduk, silang sengkarut, keliru", [
    {"word": "錯覚", "furigana": "さっかく", "romaji": "sakkaku", "meaning": "Ilusi optik / salah sangka / keliru persepsi", "level": "N1", "example": "目の錯覚で部屋が広く見える。", "example_reading": "めのさっかくでへやがひろくみえる。", "example_meaning": "Karena ilusi mata, ruangan tampak lebih luas."},
    {"word": "錯誤", "furigana": "さくご", "romaji": "sakugo", "meaning": "Kekeliruan / kekhilafan", "level": "N1", "example": "時代錯誤なルールを見直す。", "example_reading": "じだいさくごなるーるをみなおす。", "example_meaning": "Meninjau kembali aturan yang ketinggalan zaman (anakronisme)."},
    {"word": "交錯", "furigana": "こうさく", "romaji": "kousaku", "meaning": "Bercampur aduk / bersilangan", "level": "N1", "example": "希望と不安が交錯する。", "example_reading": "きぼうとふあんがこうさくする。", "example_meaning": "Harapan dan kecemasan bercampur aduk."},
    {"word": "錯乱", "furigana": "さくらん", "romaji": "sakuran", "meaning": "Kekacauan pikiran / linglung / histeris", "level": "N1", "example": "精神錯乱に陥る。", "example_reading": "せいしんさくらんにおちいる。", "example_meaning": "Jatuh ke dalam kondisi kebingungan mental."}
])

add_kanji(1, "誤", "ゴ", "あやま・る", "Salah, kekeliruan", [
    {"word": "誤解", "furigana": "ごかい", "romaji": "gokai", "meaning": "Salah paham", "level": "N3", "example": "お互いの誤解を解いた。", "example_reading": "おたがいのごかいをといた。", "example_meaning": "Menyelesaikan kesalahpahaman di antara kami."},
    {"word": "誤差", "furigana": "ごさ", "romaji": "gosa", "meaning": "Selisih kesalahan / margin of error", "level": "N2", "example": "計算の誤差を修正する。", "example_reading": "けいさんのごさをしゅうせいする。", "example_meaning": "Memperbaiki selisih margin kesalahan perhitungan."},
    {"word": "誤診", "furigana": "ごしん", "romaji": "goshin", "meaning": "Salah diagnosis medis", "level": "N1", "example": "レントゲンによって誤診を防いだ。", "example_reading": "れんとげんによってごしんをふせいだ。", "example_meaning": "Rontgen mencegah terjadinya salah diagnosis."},
    {"word": "誤字", "furigana": "ごじ", "romaji": "goji", "meaning": "Salah ketik / typo kanji", "level": "N2", "example": "メールの誤字脱字を直す。", "example_reading": "めーるのごじだつじをなおす。", "example_meaning": "Memperbaiki salah ketik dan huruf yang hilang di email."}
])

add_kanji(1, "極", "キョク、ゴク", "きわ・める、きわ・まる", "Ekstrem, kutub, puncak", [
    {"word": "極端", "furigana": "きょくたん", "romaji": "kyokutan", "meaning": "Ekstrem / berlebihan ujung ke ujung", "level": "N2", "example": "極端な意見には賛成できない。", "example_reading": "きょくたんないけんにはさんせいできない。", "example_meaning": "Saya tidak bisa setuju dengan pendapat yang ekstrem."},
    {"word": "究極", "furigana": "きゅうきょく", "romaji": "kyuukyoku", "meaning": "Puncak tertinggi / ultimate", "level": "N1", "example": "これが究極のラーメンだ。", "example_reading": "これがきゅうきょくのらーめんだ。", "example_meaning": "Inilah ramen yang paling sempurna / ultimate."},
    {"word": "積極的", "furigana": "せっきょくてき", "romaji": "sekkyokuteki", "meaning": "Proaktif / positif giat", "level": "N3", "example": "授業に積極的に参加する。", "example_reading": "じゅぎょうにせっきょくてきにさんかする。", "example_meaning": "Berpartisipasi secara proaktif di kelas."},
    {"word": "北極", "furigana": "ほっきょく", "romaji": "hokkyoku", "meaning": "Kutub Utara", "level": "N2", "example": "北極熊が生息する地域だ。", "example_reading": "ほっきょくぐまがせいそくするちいきだ。", "example_meaning": "Ini adalah wilayah tempat tinggal beruang kutub."}
])

add_kanji(1, "範", "ハン", "", "Pola, ruang lingkup, model teladan", [
    {"word": "範囲", "furigana": "はんい", "romaji": "han'i", "meaning": "Ruang lingkup / cakupan / batas wilayah", "level": "N3", "example": "テストの範囲を確認した。", "example_reading": "てすとのはんいをかくにんした。", "example_meaning": "Memastikan ruang lingkup materi tes."},
    {"word": "模範", "furigana": "もはん", "romaji": "mohan", "meaning": "Teladan / contoh panutan yang baik", "level": "N1", "example": "先輩の模範的な行動を見習う。", "example_reading": "せんぱいのもはんてきなこうどうをみならう。", "example_meaning": "Meneladani perilaku baik dari senior."},
    {"word": "師範", "furigana": "しはん", "romaji": "shihan", "meaning": "Instruktur master beladiri / guru besar", "level": "N1", "example": "柔道の師範から免状を授与された。", "example_reading": "じゅうどうのしはんからめんじょうをじゅよされた。", "example_meaning": "Diberikan sertifikat oleh master instruktur judo."}
])

add_kanji(1, "忍", "ニン", "しの・ぶ", "Sabar, menyelinap, bertahan", [
    {"word": "忍者", "furigana": "にんじゃ", "romaji": "ninja", "meaning": "Ninja", "level": "N3", "example": "忍者の里を観光した。", "example_reading": "にんじゃのさとをかんこうした。", "example_meaning": "Berwisata ke desa ninja."},
    {"word": "忍耐", "furigana": "にんたい", "romaji": "nintai", "meaning": "Kesabaran / daya tahan mental ketabahan", "level": "N1", "example": "困難を忍耐強く乗り越える。", "example_reading": "こんなんをにんたいづよくのりこえる。", "example_meaning": "Mengatasi kesulitan dengan penuh kesabaran."},
    {"word": "隠忍", "furigana": "いんにん", "romaji": "innin", "meaning": "Menahan diri / sabar tanpa mengeluh", "level": "N1", "example": "怒りを隠忍して仕事に励む。", "example_reading": "いかりをいんにんしてしごとにはげむ。", "example_meaning": "Meredam kemarahan dan fokus tekun bekerja."}
])

add_kanji(1, "看", "カン", "み・る", "Melihat, merawat, menjaga", [
    {"word": "看護", "furigana": "かんご", "romaji": "kango", "meaning": "Perawatan keperawatan pasien", "level": "N3", "example": "看護師さんが優しく世話をしてくれた。", "example_reading": "かんごしさんがやさしくせわをしてくれた。", "example_meaning": "Perawat merawat saya dengan sangat ramah."},
    {"word": "看板", "furigana": "かんばん", "romaji": "kamban", "meaning": "Papan nama toko / plang nama", "level": "N3", "example": "店の看板が遠くからでも見える。", "example_reading": "みせのかんばんがとおくからでもみえる。", "example_meaning": "Papan nama toko terlihat bahkan dari kejauhan."},
    {"word": "看過", "furigana": "かんか", "romaji": "kanka", "meaning": "Mengabaikan / membiarkan begitu saja", "level": "N1", "example": "安全基準の違反は看過できない。", "example_reading": "あんぜんきじゅんのいはんはかんかできない。", "example_meaning": "Pelanggaran standar keselamatan tidak bisa dibiarkan begitu saja."},
    {"word": "看破", "furigana": "かんぱ", "romaji": "kampa", "meaning": "Melihat tembus / membongkar muslihat", "level": "N1", "example": "相手の嘘を一瞬で看破した。", "example_reading": "あいてのうそをいっしゅんでかんぱした。", "example_meaning": "Membongkar kebohongan lawan dalam sekejap."}
])

add_kanji(1, "蠅", "ヨウ", "はえ", "Lalat", [
    {"word": "蠅取", "furigana": "はえとり", "romaji": "haetori", "meaning": "Perangkap lalat / pembasmi lalat", "level": "Umum", "example": "台所に蠅取り器を置く。", "example_reading": "だいどころにはえとりきをおく。", "example_meaning": "Meletakkan alat penangkap lalat di dapur."},
    {"word": "青蠅", "furigana": "あおばえ", "romaji": "aobae", "meaning": "Lalat hijau bangkai", "level": "Umum", "example": "夏場に青蠅が飛び交う。", "example_reading": "なつばにあおばえがとびかう。", "example_meaning": "Lalat hijau beterbangan di musim panas."},
    {"word": "蠅声", "furigana": "ようせい", "romaji": "yousei", "meaning": "Dengungan suara bising ramai", "level": "N1", "example": "蠅声のごとく雑音が広がる。", "example_reading": "ようせいのごとくざつおんがひろがる。", "example_meaning": "Suara gaduh menyebar ramai bagai dengungan kawanan lalat."}
])

add_kanji(1, "葵", "キ", "あおい", "Bunga aoi / mallow", [
    {"word": "向日葵", "furigana": "ひまわり", "romaji": "himawari", "meaning": "Bunga matahari", "level": "N2", "example": "畑一面に向日葵が咲いている。", "example_reading": "はたけいちめんにひまわりがさいている。", "example_meaning": "Bunga matahari bermekaran di seantero ladang."},
    {"word": "葵祭", "furigana": "あおいまつり", "romaji": "aoimatsuri", "meaning": "Aoi Matsuri (festival kuno megah Kyoto)", "level": "Umum", "example": "葵祭の行列を見に行った。", "example_reading": "あおいまつりのぎょうれつをみにいった。", "example_meaning": "Pergi menonton arak-arakan parade festival Aoi Matsuri."},
    {"word": "山葵", "furigana": "わさび", "romaji": "wasabi", "meaning": "Wasabi (sambal hijau pedas menyengat Jepang)", "level": "N3", "example": "生魚に山葵をつける。", "example_reading": "なまざかなにわさびをつける。", "example_meaning": "Membubuhkan wasabi pada ikan mentah (sashimi)."}
])

add_kanji(1, "倫", "リン", "", "Etika, tata moral, susila", [
    {"word": "倫理", "furigana": "りんり", "romaji": "rinri", "meaning": "Etika / norma kesusilaan", "level": "N1", "example": "医療倫理に関する講義を受ける。", "example_reading": "いりょうりんりにかんするこうぎをうける。", "example_meaning": "Mengikuti kuliah mengenai etika kedokteran."},
    {"word": "不倫", "furigana": "ふりん", "romaji": "furin", "meaning": "Perselingkuhan / asusila hubungan gelap", "level": "N2", "example": "不倫関係が発覚して問題になった。", "example_reading": "ふりんかんけいがはっかくしてもんだいになった。", "example_meaning": "Hubungan perselingkuhan terungkap dan memicu masalah."},
    {"word": "倫理観", "furigana": "りんりかん", "romaji": "rinrikan", "meaning": "Pedoman pandangan moral etika", "level": "N1", "example": "社会人として高い倫理観が求められる。", "example_reading": "しゃかいじんとしてたかいりんりかんがもとめられる。", "example_meaning": "Sebagai warga masyarakat dituntut memiliki nilai moralitas tinggi."}
])

add_kanji(1, "敦", "トン", "", "Tulus ikhlas, ramah berhati luhur", [
    {"word": "敦厚", "furigana": "とんこう", "romaji": "tonkou", "meaning": "Ramah dan tulus ikhlas budi pekertinya", "level": "N1", "example": "彼は敦厚な人柄で慕われている。", "example_reading": "かれはとんこうなひとがらでしたわれている。", "example_meaning": "Dia disayangi banyak orang karena sifatnya yang tulus dan ramah."},
    {"word": "敦賀", "furigana": "つるが", "romaji": "tsuruga", "meaning": "Tsuruga (kota pelabuhan & stasiun di Fukui)", "level": "Umum", "example": "敦賀駅で乗り換える。", "example_reading": "つるがえきでのりかえる。", "example_meaning": "Pindah kereta di stasiun Tsuruga."},
    {"word": "敦睦", "furigana": "とんぼく", "romaji": "tomboku", "meaning": "Hubungan rukun akrab harmonis", "level": "N1", "example": "両国の敦睦を深める外交方針だ。", "example_reading": "りょうこくのとんぼくをふかめるがいこうほうしんだ。", "example_meaning": "Kebijakan diplomasi untuk mempererat kerukunan kedua negara."}
])

add_kanji(1, "情", "ジョウ、セイ", "なさ・け", "Informasi, perasaan rasa, empati", [
    {"word": "情報", "furigana": "じょうほう", "romaji": "jouhou", "meaning": "Informasi / kabar berita", "level": "N3", "example": "個人情報の管理に気をつける。", "example_reading": "こじんじょうほうのかんりにきをつける。", "example_meaning": "Berhati-hati dalam mengelola data informasi pribadi."},
    {"word": "感情", "furigana": "かんじょう", "romaji": "kanjou", "meaning": "Emosi / perasaan", "level": "N3", "example": "感情的にならず冷静に話し合おう。", "example_reading": "かんじょうてきにならずれいせいにはなしあおう。", "example_meaning": "Mari berdiskusi dengan tenang tanpa terbawa emosi."},
    {"word": "表情", "furigana": "ひょうじょう", "romaji": "hyoujou", "meaning": "Raut muka / ekspresi wajah", "level": "N3", "example": "明るい表情で挨拶をした。", "example_reading": "あかるいひょうじょうであいさつをした。", "example_meaning": "Menyapa dengan raut wajah yang ceria."},
    {"word": "友情", "furigana": "ゆうじょう", "romaji": "yuujou", "meaning": "Persahabatan ikatan pertemanan", "level": "N3", "example": "彼との友情は一生の宝物だ。", "example_reading": "かれとのゆうじょうはいっしょうのたからものだ。", "example_meaning": "Persahabatan dengannya adalah harta seumur hidup."}
])

add_kanji(1, "息", "ソク", "いき", "Napas, anak lelaki, jeda", [
    {"word": "息", "furigana": "いき", "romaji": "iki", "meaning": "Napas", "level": "N4", "example": "深呼吸して息を整える。", "example_reading": "しんこきゅうしていきをととのえる。", "example_meaning": "Tarik napas dalam-dalam untuk mengatur napas."},
    {"word": "息子", "furigana": "むすこ", "romaji": "musuko", "meaning": "Anak laki-laki", "level": "N4", "example": "息子がサッカーの試合で勝った。", "example_reading": "むすこがさっかーのしあいでかった。", "example_meaning": "Anak laki-laki saya menang dalam pertandingan sepak bola."},
    {"word": "休息", "furigana": "きゅうそく", "romaji": "kyuusoku", "meaning": "Istirahat santai / jeda jeda kerja", "level": "N2", "example": "十分な休息を取ることが大切だ。", "example_reading": "じゅうぶんなきゅうそくをとることがたいせつだ。", "example_meaning": "Sangat penting untuk mengambil istirahat yang cukup."},
    {"word": "利息", "furigana": "りそく", "romaji": "risoku", "meaning": "Bunga uang simpanan atau pinjaman", "level": "N2", "example": "住宅ローンの利息を計算する。", "example_reading": "じゅうたくろーんのりそくをけいさんする。", "example_meaning": "Menghitung bunga cicilan kredit pemilikan rumah."}
])

add_kanji(1, "影", "エイ", "かげ", "Bayangan, bayang rupa", [
    {"word": "影響", "furigana": "えいきょう", "romaji": "eikyou", "meaning": "Pengaruh / imbas efek", "level": "N3", "example": "台風の影響で電車が止まった。", "example_reading": "たいふうのえいきょうででんしゃがとまった。", "example_meaning": "Akibat pengaruh angin topan, kereta berhenti beroperasi."},
    {"word": "撮影", "furigana": "さつえい", "romaji": "satsuei", "meaning": "Pemotretan / perekaman syuting foto/video", "level": "N2", "example": "美しい夕日をカメラで撮影した。", "example_reading": "うつくしいゆうひをかめらでさつえいした。", "example_meaning": "Memotret matahari terbenam yang indah dengan kamera."},
    {"word": "幻影", "furigana": "げんえい", "romaji": "gen'ei", "meaning": "Bayangan ilusi / fatamorgana", "level": "N1", "example": "過去の栄光という幻影を追う。", "example_reading": "かこのえいこうというげんえいをおう。", "example_meaning": "Mengejar ilusi bayang kejayaan masa lalu."},
    {"word": "面影", "furigana": "おもかげ", "romaji": "omokage", "meaning": "Guratan wajah kenangan / jejak rupa", "level": "N1", "example": "幼い頃の面影がまだ残っている。", "example_reading": "おさないころのおもかげがまだのこっている。", "example_meaning": "Guratan raut masa kecilnya masih tersisa."}
])

add_kanji(1, "響", "キョウ", "ひび・く", "Gema gaung getaran suara", [
    {"word": "反響", "furigana": "はんきょう", "romaji": "hankyou", "meaning": "Gema / reaksi respons publik", "level": "N1", "example": "SNSで大きな反響があった。", "example_reading": "えすえぬえすでおおきなはんきょうがあった。", "example_meaning": "Mendapat respons yang sangat besar di media sosial."},
    {"word": "音響", "furigana": "おんきょう", "romaji": "onkyou", "meaning": "Akustik tata bunyi / tata suara", "level": "N1", "example": "音響効果で映画の迫力が増した。", "example_reading": "おんきょうこうかでえいがのはくりょくがました。", "example_meaning": "Efek tata suara meningkatkan keseruan film."},
    {"word": "交響曲", "furigana": "こうきょうきょく", "romaji": "koukyoukyoku", "meaning": "Simfoni musik orkestra klasik", "level": "N1", "example": "交響曲の演奏会に出かけた。", "example_reading": "こうきょうきょくのえんそうかいにでかけた。", "example_meaning": "Pergi menghadiri konser pertunjukan simfoni."}
])

add_kanji(1, "愉", "ユ", "たの・しい", "Senang riang gembira", [
    {"word": "愉快", "furigana": "ゆかい", "romaji": "yukai", "meaning": "Menyenangkan / lucu menghibur / riang", "level": "N2", "example": "愉快な話を聞いて大笑いした。", "example_reading": "ゆかいなはなしをきいておおわらいした。", "example_meaning": "Tertawa terbahak-bahak mendengar cerita yang lucu menghibur."},
    {"word": "愉悦", "furigana": "ゆえつ", "romaji": "yuetsu", "meaning": "Sukacita batin / kegembiraan hati", "level": "N1", "example": "勝利の愉悦を味わう。", "example_reading": "しょうりのゆえつをあじわう。", "example_meaning": "Mengecap sukacita batin atas kemenangan."},
    {"word": "愉楽", "furigana": "ゆらく", "romaji": "yuraku", "meaning": "Kenikmatan ria / kesenangan santai", "level": "N1", "example": "週末の愉楽を満喫した。", "example_reading": "しゅうまつのゆらくをまんきつした。", "example_meaning": "Menikmati sepuasnya kesenangan di akhir pekan."}
])

add_kanji(1, "快", "カイ", "こころよ・い", "Nyaman, bugar, lekas sembuh", [
    {"word": "快適", "furigana": "かいてき", "romaji": "kaiteki", "meaning": "Nyaman enak / kondusif", "level": "N3", "example": "エアコンのおかげで部屋が快適だ。", "example_reading": "えあこんなおかげでへやがかいてきだ。", "example_meaning": "Berkat AC ruangannya sangat nyaman."},
    {"word": "快晴", "furigana": "かいせい", "romaji": "kaisei", "meaning": "Cerah benderang tanpa awan", "level": "N3", "example": "秋晴れの気持ちの良い快晴だ。", "example_reading": "あきばれのきもちのよいかいせいだ。", "example_meaning": "Hari yang cerah benderang dan menyenangkan di musim gugur."},
    {"word": "爽快", "furigana": "そうかい", "romaji": "soukai", "meaning": "Segar bugar menyegarkan", "level": "N1", "example": "山頂で爽快な風を感じた。", "example_reading": "さんちょうでそうかいなかぜをかんじた。", "example_meaning": "Merasakan hembusan angin yang menyegarkan di puncak gunung."},
    {"word": "快復", "furigana": "かいふく", "romaji": "kaifuku", "meaning": "Pemulihan kondisi kesehatan", "level": "N2", "example": "病気が順調に快復している。", "example_reading": "びょうきがじゅんちょうにかいふくしている。", "example_meaning": "Penyakitnya pulih membaik dengan lancar."}
])

add_kanji(1, "素", "ソ、ス", "もと", "Polos, unsur elemen, murni", [
    {"word": "素敵", "furigana": "すてき", "romaji": "suteki", "meaning": "Bagus mempesona / luar biasa indah", "level": "N4", "example": "素敵なプレゼントをありがとう。", "example_reading": "すてきなぷれぜんとをありがとう。", "example_meaning": "Terima kasih atas kado yang sangat bagus ini."},
    {"word": "素直", "furigana": "すなお", "romaji": "sunao", "meaning": "Jujur tulus / penurut tidak keras kepala", "level": "N3", "example": "素直な心でアドバイスを聞く。", "example_reading": "すなおなこころであどばいすをきく。", "example_meaning": "Mendengarkan nasihat dengan hati yang terbuka dan tulus."},
    {"word": "要素", "furigana": "ようそ", "romaji": "youso", "meaning": "Unsur / elemen pembentuk penting", "level": "N2", "example": "デザインの基本要素を学ぶ。", "example_reading": "でざいんのきほんようそをまなぶ。", "example_meaning": "Mempelajari unsur-unsur dasar desain."},
    {"word": "素朴", "furigana": "そぼく", "romaji": "soboku", "meaning": "Sederhana polos alami tanpa riasan", "level": "N1", "example": "素朴な味わいの郷土料理だ。", "example_reading": "そぼくなあじわいのきょうどりょうリーダーだ。", "example_meaning": "Masakan tradisional daerah dengan cita rasa sederhana alami."}
])

# ==========================================
# MINGGU 2 (28 Kanji)
# 促、編、娯、魅、視、争、層、刊、巨、競、浮、蓄、河、秘、歴、遭、幻、襲、粉、源、鉱、漠、徴、睡、嫌、署、悔、隠
# ==========================================
add_kanji(2, "促", "ソク", "うなが・す", "Mendorong, mendesak, mempercepat", [
    {"word": "促進", "furigana": "そくしん", "romaji": "sokushin", "meaning": "Percepatan / promosi peningkatan", "level": "N2", "example": "観光の促進を図るイベントだ。", "example_reading": "かんこうのそくしんをはかるいべんとだ。", "example_meaning": "Acara yang bertujuan untuk mendorong promosi pariwisata."},
    {"word": "催促", "furigana": "さいそく", "romaji": "saisoku", "meaning": "Mendesak / menagih tenggat waktu", "level": "N2", "example": "家賃の支払いを催促された。", "example_reading": "やちんのしはらいをさいそくされた。", "example_meaning": "Saya ditagih untuk pembayaran uang sewa rumah."},
    {"word": "促音", "furigana": "そくおん", "romaji": "sokuon", "meaning": "Konsonan rangkap (huruf tsu kecil っ)", "level": "N1", "example": "促音の発音練習をする。", "example_reading": "そくおんのはつおんれんしゅうをする。", "example_meaning": "Berlatih pelafalan konsonan rangkap (sokuon)."}
])

add_kanji(2, "編", "ヘン", "あ・む", "Menyusun, mengedit, merajut", [
    {"word": "編集", "furigana": "へんしゅう", "romaji": "henshuu", "meaning": "Pengeditan / penyuntingan karya naskah", "level": "N2", "example": "動画をパソコンで編集する。", "example_reading": "どうがをぱそこんでへんしゅうする。", "example_meaning": "Mengedit video di komputer."},
    {"word": "短編", "furigana": "たんぺん", "romaji": "tampen", "meaning": "Cerpen / karya pendek naskah singkat", "level": "N1", "example": "芥川龍之介の短編小説を読む。", "example_reading": "あくたがわりゅうのすけのたんぺんしょうせつをよむ。", "example_meaning": "Membaca cerita pendek karya Ryunosuke Akutagawa."},
    {"word": "編成", "furigana": "へんせい", "romaji": "hensei", "meaning": "Penyusunan susunan formasi tim/jadwal", "level": "N1", "example": "電車の特別ダイヤを編成する。", "example_reading": "でんしゃのとくべつだいやをへんせいする。", "example_meaning": "Menyusun jadwal keberangkatan kereta khusus."},
    {"word": "前編", "furigana": "ぜんぺん", "romaji": "zempen", "meaning": "Bagian pertama / volume awal", "level": "N2", "example": "映画の前編を観終わった。", "example_reading": "えいがのぜんぺんをみおわった。", "example_meaning": "Selesai menonton film bagian pertama."}
])

add_kanji(2, "娯", "ゴ", "", "Hiburan, bersenang-senang", [
    {"word": "娯楽", "furigana": "ごらく", "romaji": "goraku", "meaning": "Hiburan / rekreasi pelipur penat", "level": "N3", "example": "映画鑑賞が私の唯一の娯楽だ。", "example_reading": "えいがかんしょうがわたしのゆいいつのごらくだ。", "example_meaning": "Menonton film adalah satu-satunya hiburan saya."},
    {"word": "娯楽室", "furigana": "ごらくしつ", "romaji": "gorakushitsu", "meaning": "Ruang rekreasi / ruang permainan", "level": "Umum", "example": "ホテルの娯楽室で卓球をした。", "example_reading": "ほてるのごらくしつでたっきゅうをした。", "example_meaning": "Bermain tenis meja di ruang rekreasi hotel."}
])

add_kanji(2, "魅", "ミ", "", "Pesona pikat daya tarik", [
    {"word": "魅力", "furigana": "みりょく", "romaji": "miryoku", "meaning": "Daya tarik / pesona pikat", "level": "N3", "example": "この街には多くの魅力がある。", "example_reading": "このまちにはおおくのみりょくがある。", "example_meaning": "Kota ini memiliki banyak daya tarik."},
    {"word": "魅了", "furigana": "みりょう", "romaji": "miryou", "meaning": "Mempesona memikat hati", "level": "N1", "example": "彼女の美しい歌声に魅了された。", "example_reading": "かのじょのうつくしいうたごえにみりょうされた。", "example_meaning": "Terpesona terpikat oleh suara nyanyiannya yang merdu."},
    {"word": "魅惑", "furigana": "みわく", "romaji": "miwaku", "meaning": "Pesona pikat menggoda", "level": "N1", "example": "魅惑的な香りに引き寄せられる。", "example_reading": "みわくてきなかおりにひきよせられる。", "example_meaning": "Tertarik oleh aroma wangi yang memikat menggoda."}
])

add_kanji(2, "視", "シ", "み・る", "Melihat, sudut pandang, memeriksa", [
    {"word": "視点", "furigana": "してん", "romaji": "shiten", "meaning": "Sudut pandang / perspektif", "level": "N2", "example": "新しい視点から問題を考える。", "example_reading": "あたらしいしてんからもんだいをかんがえる。", "example_meaning": "Memikirkan masalah dari perspektif baru."},
    {"word": "視野", "furigana": "しや", "romaji": "shiya", "meaning": "Wawasan / bidang pandangan mata", "level": "N2", "example": "留学して視野を広げたい。", "example_reading": "りゅうがくしてしやをひろげたい。", "example_meaning": "Saya ingin memperluas wawasan dengan belajar di luar negeri."},
    {"word": "無視", "furigana": "むし", "romaji": "mushi", "meaning": "Mengabaikan / menyepelekan", "level": "N3", "example": "赤信号を無視してはいけない。", "example_reading": "あかしんごうをむししてはいけない。", "example_meaning": "Tidak boleh mengabaikan lampu merah."},
    {"word": "監視", "furigana": "かんし", "romaji": "kanshi", "meaning": "Pengawasan / pemantauan ketat", "level": "N1", "example": "防犯カメラで24時間監視している。", "example_reading": "ぼうはんかめらでにじゅうよじかんかんししている。", "example_meaning": "Dipantau 24 jam dengan kamera pengawas (CCTV)."}
])

add_kanji(2, "争", "ソウ", "あらそ・う", "Bersaing, bertengkar, perang", [
    {"word": "戦争", "furigana": "せんそう", "romaji": "sensou", "meaning": "Perang / pertempuran bersenjata", "level": "N4", "example": "世界中から戦争がなくなることを祈る。", "example_reading": "せかいじゅうからせんそうがなくなることをいのる。", "example_meaning": "Mendoakan agar perang lenyap dari seluruh dunia."},
    {"word": "競争", "furigana": "きょうそう", "romaji": "kyousou", "meaning": "Persaingan / kompetisi", "level": "N3", "example": "市場での価格競争が激しい。", "example_reading": "しじょうでのかかくきょうそうがはげしい。", "example_meaning": "Persaingan harga di pasar sangat ketat."},
    {"word": "論争", "furigana": "ろんそう", "romaji": "ronsou", "meaning": "Perdebatan / polemik sengketa", "level": "N1", "example": "政策を巡って激しい論争が起きた。", "example_reading": "せいさくをめぐってはげしいろんそうがおきた。", "example_meaning": "Terjadi perdebatan sengit mengenai kebijakan tersebut."},
    {"word": "争議", "furigana": "そうぎ", "romaji": "sougi", "meaning": "Sengketa / perselisihan buruh", "level": "N1", "example": "労働争議を円満に解決した。", "example_reading": "ろうどうそうぎをえんまんにかいけつした。", "example_meaning": "Menyelesaikan perselisihan perburuhan dengan damai."}
])

add_kanji(2, "層", "ソウ", "", "Lapisan, strata tingkatan", [
    {"word": "階層", "furigana": "かいそう", "romaji": "kaisou", "meaning": "Lapisan strata sosial / hierarki", "level": "N1", "example": "社会の様々な階層の人々が集まる。", "example_reading": "しゃかいのさまざまなかいそうのひとびとがあつまる。", "example_meaning": "Orang-orang dari berbagai lapisan strata sosial berkumpul."},
    {"word": "地層", "furigana": "ちそう", "romaji": "chisou", "meaning": "Lapisan tanah geologis", "level": "N2", "example": "崖の断面に美しい地層が見える。", "example_reading": "がけのだんめんにうつくしいちそうがみえる。", "example_meaning": "Terlihat lapisan tanah yang indah pada tebing curam."},
    {"word": "一層", "furigana": "いっそう", "romaji": "issou", "meaning": "Semakin / jauh lebih bertambah", "level": "N2", "example": "寒さが一層厳しくなってきた。", "example_reading": "さむさがいっそうきびしくなってきた。", "example_meaning": "Hawa dingin sudah semakin menusuk."},
    {"word": "中間層", "furigana": "ちゅうかんそう", "romaji": "chuukansou", "meaning": "Kelas menengah strata ekonomi", "level": "N1", "example": "中間層を増やす経済対策を行う。", "example_reading": "ちゅうかんそうをふやすけいざいたいさくをおこなう。", "example_meaning": "Menjalankan kebijakan ekonomi untuk menumbuhkan kelas menengah."}
])

add_kanji(2, "刊", "カン", "", "Menerbitkan, cetak edisi", [
    {"word": "刊行", "furigana": "かんこう", "romaji": "kankou", "meaning": "Publikasi terbitan buku naskah", "level": "N1", "example": "記念誌を刊行することになった。", "example_reading": "きねんしをかんこうすることになった。", "example_meaning": "Diputuskan untuk menerbitkan majalah peringatan."},
    {"word": "朝刊", "furigana": "ちょうかん", "romaji": "choukan", "meaning": "Koran edisi pagi", "level": "N2", "example": "毎朝朝刊を隅々まで読む。", "example_reading": "まいあさちょうかんをすみずみまでよむ。", "example_meaning": "Membaca koran pagi setiap pagi sampai tuntas."},
    {"word": "週刊", "furigana": "しゅうかん", "romaji": "shuukan", "meaning": "Terbitan mingguan majalah", "level": "N2", "example": "週刊誌の最新号を買った。", "example_reading": "しゅうかんしのさいしんごうをかった。", "example_meaning": "Membeli edisi terbaru dari majalah mingguan."},
    {"word": "休刊", "furigana": "きゅうかん", "romaji": "kyuukan", "meaning": "Jeda libur terbit koran majalah", "level": "N1", "example": "明日は新聞の休刊日です。", "example_reading": "あすはしんぶんのきゅうかんびです。", "example_meaning": "Besok adalah hari libur terbit koran."}
])

add_kanji(2, "巨", "キョ", "", "Raksasa, mahabesar", [
    {"word": "巨大", "furigana": "きょだい", "romaji": "kyodai", "meaning": "Raksasa mahabesar luar biasa", "level": "N3", "example": "海に巨大なクジラが現れた。", "example_reading": "うみにきょだいなくじらがあらわれた。", "example_meaning": "Seekor paus raksasa muncul di lautan."},
    {"word": "巨人", "furigana": "きょじん", "romaji": "kyojin", "meaning": "Raksasa / tokoh raksasa industri", "level": "N2", "example": "童話に出てくる巨人の城。", "example_reading": "どうわにでてくるきょじんのしろ。", "example_meaning": "Kastel raksasa yang muncul dalam cerita dongeng."},
    {"word": "巨額", "furigana": "きょがく", "romaji": "kyogaku", "meaning": "Jumlah dana nominal raksasa", "level": "N1", "example": "巨額の資金を投資する。", "example_reading": "きょがくのしきんをとうしする。", "example_meaning": "Menginvestasikan dana dalam jumlah fantastis."},
    {"word": "巨匠", "furigana": "きょしょう", "romaji": "kyoshou", "meaning": "Sang maestro besar seniman", "level": "N1", "example": "絵画の巨匠の個展を見に行く。", "example_reading": "かいがのきょしょうのこてんをみにいく。", "example_meaning": "Pergi melihat pameran tunggal karya sang maestro lukis."}
])

add_kanji(2, "競", "キョウ、ケイ", "きそ・う", "Bersaing, bertanding, pacuan", [
    {"word": "競技", "furigana": "きょうぎ", "romaji": "kyougi", "meaning": "Pertandingan olahraga / cabor", "level": "N2", "example": "オリンピックの新競技を観戦する。", "example_reading": "おりんぴっくのしんきょうぎをかんせんする。", "example_meaning": "Menonton cabor baru di olimpiade."},
    {"word": "競馬", "furigana": "けいば", "romaji": "keiba", "meaning": "Pacuan kuda", "level": "N2", "example": "週末に競馬場へ足を運んだ。", "example_reading": "しゅうまつにけいばじょうへあしをはこんだ。", "example_meaning": "Pergi berkunjung ke arena pacuan kuda di akhir pekan."},
    {"word": "競走", "furigana": "きょうそう", "romaji": "kyousou", "meaning": "Lomba adu lari", "level": "N3", "example": "徒競走で一等賞をとった。", "example_reading": "ときょうそうでいっとうしょうをとった。", "example_meaning": "Meraih juara pertama dalam lomba lari cepat."},
    {"word": "競売", "furigana": "けいばい", "romaji": "keibai", "meaning": "Lelang penjualan umum", "level": "N1", "example": "差し押さえられた土地が競売にかけられた。", "example_reading": "さしおさえられたとちがけいばいにかけられた。", "example_meaning": "Tanah yang disita dilelang ke publik."}
])

add_kanji(2, "浮", "フ", "う・く、う・かぶ", "Terapung, melayang, muncul ke atas", [
    {"word": "浮上", "furigana": "ふじょう", "romaji": "fujou", "meaning": "Naik mencuat ke permukaan", "level": "N1", "example": "潜水艦が海面に浮上した。", "example_reading": "せんすいかんがかいめんにふじょうした。", "example_meaning": "Kapal selam naik muncul ke permukaan laut."},
    {"word": "浮気", "furigana": "うわき", "romaji": "uwaki", "meaning": "Selingkuh / main mata plin-plan", "level": "N2", "example": "彼の浮気が原因で別れた。", "example_reading": "かれのうわきがげんいんでわかれた。", "example_meaning": "Putus gara-gara dia berselingkuh."},
    {"word": "浮沈", "furigana": "ふちん", "romaji": "fuchin", "meaning": "Pasang surut nasib / tenggelam terapung", "level": "N1", "example": "企業の浮沈は経営陣の判断次第だ。", "example_reading": "きぎょうのふちんはけいえいじんのはんだんしだいだ。", "example_meaning": "Pasang surut jatuh bangun perusahaan tergantung keputusan manajemen."},
    {"word": "浮力", "furigana": "ふりょく", "romaji": "furyoku", "meaning": "Gaya apung hidrolik", "level": "N1", "example": "水中の物体には浮力が働く。", "example_reading": "すいちゅうのぶったいにはふりょくがはたらく。", "example_meaning": "Benda di dalam air terkena gaya apung."}
])

add_kanji(2, "蓄", "チク", "たくわ・える", "Menimbun, mengumpulkan cadangan", [
    {"word": "蓄積", "furigana": "ちくせき", "romaji": "chikuseki", "meaning": "Akumulasi / penumpukan data pengalaman", "level": "N1", "example": "長年の経験と知識の蓄積がある。", "example_reading": "ながねんのけいけんとちしきのちくせきがある。", "example_meaning": "Memiliki akumulasi pengalaman dan pengetahuan bertahun-tahun."},
    {"word": "貯蓄", "furigana": "ちょちく", "romaji": "chochiku", "meaning": "Tabungan simpanan dana simpanan", "level": "N2", "example": "将来のために毎月貯蓄している。", "example_reading": "しょうらいのためにまいつきちょちくしている。", "example_meaning": "Menabung setiap bulan demi masa depan."},
    {"word": "蓄電", "furigana": "ちくでん", "romaji": "chikuden", "meaning": "Penyimpanan daya baterai kelistrikan", "level": "N1", "example": "太陽光の電気を蓄電池に蓄電する。", "example_reading": "たいようこうのでんきをちくでんちにちくでんする。", "example_meaning": "Menyimpan listrik tenaga surya ke dalam baterai akumulator."}
])

add_kanji(2, "河", "カ", "かわ", "Sungai, aliran air besar", [
    {"word": "河川", "furigana": "かせん", "romaji": "kasen", "meaning": "Sungai-sungai perairan", "level": "N2", "example": "大雨で河川の水位が急激に上昇した。", "example_reading": "おおあめでかせんのすいいがきゅうげきにじょうしょうした。", "example_meaning": "Permukaan air sungai-sungai naik drastis akibat hujan lebat."},
    {"word": "銀河", "furigana": "ぎんが", "romaji": "ginga", "meaning": "Galaksi Bimasakti", "level": "N2", "example": "夜空に天の川銀河が輝いている。", "example_reading": "よぞらにあまのがわぎんががかがやいている。", "example_meaning": "Galaksi Bimasakti bersinar di langit malam."},
    {"word": "運河", "furigana": "うんが", "romaji": "unga", "meaning": "Kanal terusan jalur kapal air", "level": "N1", "example": "スエズ運河を多くの貨物船が通る。", "example_reading": "すえずうんがおおおくのかもつせんがとおる。", "example_meaning": "Banyak kapal kargo melintasi Terusan Suez."},
    {"word": "河童", "furigana": "かっぱ", "romaji": "kappa", "meaning": "Kappa (makhluk mitologi air Jepang)", "level": "Umum", "example": "河童の伝説が残る池を訪れた。", "example_reading": "かっぱのでんせつがのこるいけをおとずれた。", "example_meaning": "Mengunjungi kolam tempat legenda makhluk kappa tersisa."}
])

add_kanji(2, "秘", "ヒ", "ひ・める", "Rahasia, sembunyi", [
    {"word": "秘密", "furigana": "ひみつ", "romaji": "himitsu", "meaning": "Rahasia rahasia", "level": "N3", "example": "この話は絶対に秘密にしてください。", "example_reading": "このはなしはぜったいにひみつにしてください。", "example_meaning": "Tolong rahasiakan cerita ini sama sekali."},
    {"word": "秘書", "furigana": "ひしょ", "romaji": "hisho", "meaning": "Sekretaris kantor pimpinan", "level": "N2", "example": "社長秘書としてスケジュールを管理する。", "example_reading": "しゃちょうひしょとしてすけじゅーるをかんりする。", "example_meaning": "Mengelola jadwal kerja sebagai sekretaris direktur."},
    {"word": "秘訣", "furigana": "ひけつ", "romaji": "hiketsu", "meaning": "Resep rahasia / kunci kiat sukses", "level": "N1", "example": "長寿の秘訣は毎朝の散歩だ。", "example_reading": "ちょうじゅのひけつはまいあさのさんぽだ。", "example_meaning": "Kunci rahasia umur panjang adalah jalan pagi setiap hari."},
    {"word": "神秘", "furigana": "しんぴ", "romaji": "shimpi", "meaning": "Misteri sakral gaib", "level": "N1", "example": "自然の神秘に感動した。", "example_reading": "しぜんのしんぴにかんどうした。", "example_meaning": "Terharu takjub oleh keagungan misteri alam semesta."}
])

add_kanji(2, "歴", "レキ", "", "Riwayat, sejarah, lewat masa", [
    {"word": "歴史", "furigana": "れきし", "romaji": "rekishi", "meaning": "Sejarah masa lalu", "level": "N4", "example": "日本の古い歴史に興味がある。", "example_reading": "にほんのふるいれきしにきょうみがある。", "example_meaning": "Tertarik dengan sejarah kuno Jepang."},
    {"word": "履歴", "furigana": "りれき", "romaji": "rireki", "meaning": "Riwayat rekam jejak / history log", "level": "N2", "example": "ブラウザの閲覧履歴を削除した。", "example_reading": "ぶらうざのえつらんりれきをさくじょした。", "example_meaning": "Menghapus riwayat penelusuran di browser."},
    {"word": "経歴", "furigana": "けいれき", "romaji": "keireki", "meaning": "Perjalanan karier pekerjaan", "level": "N2", "example": "彼の素晴らしい経歴に感銘を受けた。", "example_reading": "かれのすばらしいけいれきにかんめいをうけた。", "example_meaning": "Terkesan dengan perjalanan kariernya yang luar biasa."},
    {"word": "学歴", "furigana": "がくれき", "romaji": "gakureki", "meaning": "Riwayat jenjang pendidikan", "level": "N2", "example": "学歴よりも実力が重視される。", "example_reading": "がくれきよりもじつりょくがじゅうしされる。", "example_meaning": "Keahlian nyata lebih diutamakan daripada latar belakang pendidikan."}
])

add_kanji(2, "遭", "ソウ", "あ・う", "Mengalami musibah, berpapasan tak terduga", [
    {"word": "遭遇", "furigana": "そうぐう", "romaji": "souguu", "meaning": "Perjumpaan tak terduga berhadapan", "level": "N1", "example": "山道で野生のクマに遭遇した。", "example_reading": "やまみちでやせいのくまにそうぐうした。", "example_meaning": "Berpapasan mendadak dengan beruang liar di jalan setapak gunung."},
    {"word": "遭難", "furigana": "そうなん", "romaji": "sounan", "meaning": "Musibah kecelakaan / tersesat di gunung/laut", "level": "N2", "example": "冬山で遭難した登山隊が無事救助された。", "example_reading": "ふゆやまですうなんしたとざんたいがぶじきゅうじょされた。", "example_meaning": "Tim pendaki yang celaka di gunung salju berhasil diselamatkan dengan selamat."}
])

add_kanji(2, "幻", "ゲン", "まぼろし", "Ilusi angan semu khayalan", [
    {"word": "幻想", "furigana": "げんそう", "romaji": "gensou", "meaning": "Fantasi ilusi bayangan angan", "level": "N1", "example": "幻想的な光景に目を奪われた。", "example_reading": "げんそうてきなこうけいにめをうばわれた。", "example_meaning": "Terpana oleh pemandangan indah yang fantastis bagai mimpi."},
    {"word": "幻覚", "furigana": "げんかく", "romaji": "genkaku", "meaning": "Halusinasi panca indra", "level": "N1", "example": "高熱で幻覚が見えた。", "example_reading": "こうねつでげんかくがみえた。", "example_meaning": "Mengalami halusinasi akibat demam tinggi."},
    {"word": "夢幻", "furigana": "むげん", "romaji": "mugen", "meaning": "Khayalan mimpi dan angan", "level": "N1", "example": "人生は夢幻の如くなり。", "example_reading": "じんせいはむげんのごとくなり。", "example_meaning": "Hidup bagaikan mimpi dan angan semu."},
    {"word": "幻影", "furigana": "げんえい", "romaji": "gen'ei", "meaning": "Bayangan semu fatamorgana", "level": "N1", "example": "目の前に幻影がちらついた。", "example_reading": "めのまえにげんえいがちらついた。", "example_meaning": "Bayangan semu berkelebat di depan mata."}
])

add_kanji(2, "襲", "シュウ", "おそ・う", "Menyerang, menyergap, mewarisi", [
    {"word": "襲撃", "furigana": "しゅうげき", "romaji": "shuugeki", "meaning": "Serangan mendadak serbuan", "level": "N1", "example": "敵の奇襲攻撃から基地を守った。", "example_reading": "てきのきしゅうこうげきからきちをまもった。", "example_meaning": "Melindungi pangkalan dari serangan mendadak musuh."},
    {"word": "逆襲", "furigana": "ぎゃくしゅう", "romaji": "gyakushuu", "meaning": "Serangan balik perlawanan balik", "level": "N1", "example": "後半戦でチームが見事な逆襲を見せた。", "example_reading": "こうはんせんでちーむがみごとなぎゃくしゅうをみせた。", "example_meaning": "Di babak kedua tim memperlihatkan serangan balik yang brilian."},
    {"word": "急襲", "furigana": "きゅうしゅう", "romaji": "kyuushuu", "meaning": "Serbuan kilat mendadak", "level": "N1", "example": "深夜の急襲により混乱が生じた。", "example_reading": "しんやのきゅうしゅうによりこんらんがしょうじた。", "example_meaning": "Serbuan mendadak di tengah malam memicu kekacauan."},
    {"word": "世襲", "furigana": "せしゅう", "romaji": "seshuu", "meaning": "Warisan turun temurun dinasti keluarga", "level": "N1", "example": "政治家の世襲制について議論が交わされる。", "example_reading": "せいじかのせしゅうせいについてぎろんがかわされる。", "example_meaning": "Perdebatan diperbincangkan tentang sistem dinasti turun temurun politisi."}
])

add_kanji(2, "粉", "フン", "こ、こな", "Tepung, bubuk, serbuk", [
    {"word": "小麦粉", "furigana": "こむぎこ", "romaji": "komugiko", "meaning": "Tepung terigu", "level": "N3", "example": "小麦粉を使ってパンを焼く。", "example_reading": "こむぎこをつかってぱんをやく。", "example_meaning": "Membuat memanggang roti menggunakan tepung terigu."},
    {"word": "花粉", "furigana": "かふん", "romaji": "kafun", "meaning": "Serbuk sari bunga", "level": "N2", "example": "春はスギの花粉が飛ぶ季節だ。", "example_reading": "はるはすぎのかふんがとぶきせつだ。", "example_meaning": "Musim semi adalah masa serbuk sari pohon cedar berterbangan."},
    {"word": "粉末", "furigana": "ふんまつ", "romaji": "fummatsu", "meaning": "Bubuk serbuk halus", "level": "N2", "example": "粉末の緑茶をお湯に溶かす。", "example_reading": "ふんまつのりょくちゃをおゆにとかす。", "example_meaning": "Melarutkan bubuk teh hijau ke dalam air panas."},
    {"word": "粉砕", "furigana": "ふんさい", "romaji": "funsai", "meaning": "Menghancurkan melumatkan berkeping-keping", "level": "N1", "example": "大きな岩を機械で粉砕する。", "example_reading": "おおきないわをきかいでふんさいする。", "example_meaning": "Menghancurkan batu besar menggunakan mesin."}
])

add_kanji(2, "源", "ゲン", "みなもと", "Sumber, hulu mata air, asal mula", [
    {"word": "起源", "furigana": "きげん", "romaji": "kigen", "meaning": "Asal usul cikal bakal permulaan", "level": "N2", "example": "人類の起源を探る研究だ。", "example_reading": "じんるいのきげんをさぐるけんきゅうだ。", "example_meaning": "Penelitian yang meneliti asal usul mula manusia."},
    {"word": "資源", "furigana": "しげん", "romaji": "shigen", "meaning": "Sumber daya alam", "level": "N3", "example": "天然資源を大切に活用する。", "example_reading": "てんねんしげんをたいせつにかつようする。", "example_meaning": "Memanfaatkan sumber daya alam secara bijak."},
    {"word": "電源", "furigana": "でんげん", "romaji": "dengen", "meaning": "Sumber daya listrik / tombol power", "level": "N3", "example": "パソコンの電源を切るのを忘れた。", "example_reading": "ぱそこのでんげんをきるのをわすれた。", "example_meaning": "Lupa mematikan tombol daya power komputer."},
    {"word": "語源", "furigana": "ごげん", "romaji": "gogen", "meaning": "Etimologi asal mula kata", "level": "N1", "example": "漢字の語源を辞書で調べる。", "example_reading": "かんじのごげんをじしょでしらべる。", "example_meaning": "Mencari etimologi asal mula kanji di kamus."}
])

add_kanji(2, "鉱", "コウ", "", "Tambang, mineral, bijih", [
    {"word": "鉱物", "furigana": "こうぶつ", "romaji": "koubutsu", "meaning": "Mineral tambang", "level": "N2", "example": "博物館で珍しい鉱物を見た。", "example_reading": "はくぶつかんでめずらしいこうぶつをみた。", "example_meaning": "Melihat mineral langka di museum."},
    {"word": "鉱山", "furigana": "こうざん", "romaji": "kouzan", "meaning": "Pertambangan / gunung tambang", "level": "N2", "example": "かつて金が採れた有名な鉱山だ。", "example_reading": "かつてきんがとれたゆうめいなこうざんだ。", "example_meaning": "Tambang terkenal tempat emas pernah ditambang tempo dulu."},
    {"word": "炭鉱", "furigana": "たんこう", "romaji": "tankou", "meaning": "Tambang batu bara", "level": "N1", "example": "炭鉱の跡地が観光地になっている。", "example_reading": "たんこうのあとちがかんこうちになっている。", "example_meaning": "Lahan bekas tambang batu bara menjadi tempat wisata."},
    {"word": "鉱石", "furigana": "こうせき", "romaji": "kouseki", "meaning": "Bijih batu tambang", "level": "N1", "example": "鉄の鉱石を精錬して鋼を作る。", "example_reading": "てつのこうせきをせいれんしてはがねをつくる。", "example_meaning": "Memurnikan bijih besi untuk menghasilkan baja."}
])

add_kanji(2, "漠", "バク", "", "Gurun pasir, samar-samar luas", [
    {"word": "砂漠", "furigana": "さばく", "romaji": "sabaku", "meaning": "Gurun pasir", "level": "N3", "example": "サハラ砂漠は世界最大級の砂漠だ。", "example_reading": "さはらさばくわせかいさいだいきゅうのさばくだ。", "example_meaning": "Gurun Sahara adalah salah satu gurun terbesar di dunia."},
    {"word": "漠然", "furigana": "ばくぜん", "romaji": "bakuzen", "meaning": "Samar-samar / tidak jelas belum pasti", "level": "N1", "example": "将来について漠然とした不安を抱く。", "example_reading": "しょうらいについてばくぜんとしたふあんをいだく。", "example_meaning": "Menyimpan kecemasan yang samar-samar akan masa depan."},
    {"word": "広漠", "furigana": "こうばく", "romaji": "koubaku", "meaning": "Luas membentang sejauh mata memandang", "level": "N1", "example": "広漠たる大平原が広がっている。", "example_reading": "こうばくたるだいへいげんがひろがっている。", "example_meaning": "Padang rumput raya yang luas membentang terhampar."}
])

add_kanji(2, "徴", "チョウ", "", "Ciri khas, lambang tanda, pungutan", [
    {"word": "特徴", "furigana": "とくちょう", "romaji": "tokuchou", "meaning": "Ciri khas keistimewaan", "level": "N3", "example": "この商品の特徴を説明してください。", "example_reading": "このしょうひんのとくちょうをせつめいしてください。", "example_meaning": "Tolong jelaskan ciri khas keistimewaan produk ini."},
    {"word": "象徴", "furigana": "しょうちょう", "romaji": "shouchou", "meaning": "Simbol lambang", "level": "N2", "example": "富士山は日本の象徴だ。", "example_reading": "ふじさんはにほんのしょうちょうだ。", "example_meaning": "Gunung Fuji adalah simbol negara Jepang."},
    {"word": "徴収", "furigana": "ちょうしゅう", "romaji": "choushuu", "meaning": "Pemungutan penarikan iuran/pajak", "level": "N1", "example": "会費を会員から徴収する。", "example_reading": "かいひをかいいんからちょうしゅうする。", "example_meaning": "Memungut iuran dari para anggota."},
    {"word": "徴候", "furigana": "ちょうこう", "romaji": "choukou", "meaning": "Gejala pertanda sinyal awal", "level": "N1", "example": "景気回復の徴候が現れている。", "example_reading": "けいきかいふくのちょうこうがあらわれている。", "example_meaning": "Pertanda pemulihan ekonomi mulai terlihat."}
])

add_kanji(2, "睡", "スイ", "ねむ・る", "Tidur", [
    {"word": "睡眠", "furigana": "すいみん", "romaji": "suimin", "meaning": "Tidur waktu tidur", "level": "N3", "example": "健康のために十分な睡眠をとる。", "example_reading": "けんこうのためにじゅうぶんなすいみんをとる。", "example_meaning": "Tidur yang cukup demi menjaga kesehatan."},
    {"word": "熟睡", "furigana": "じゅくすい", "romaji": "jukusui", "meaning": "Tidur nyenyak pulas", "level": "N2", "example": "昨晩は熟睡できたので気分爽快だ。", "example_reading": "さくばんはじゅくすいできたのできぶんそうかいだ。", "example_meaning": "Perasaan segar bugar karena semalam bisa tidur nyenyak."},
    {"word": "昏睡", "furigana": "こんすい", "romaji": "konsui", "meaning": "Koma tidak sadarkan diri mendalam", "level": "N1", "example": "事故の後、昏睡状態が続いている。", "example_reading": "じこのあと、こんすいじょうたいがつづいている。", "example_meaning": "Setelah kecelakaan, kondisi koma masih berlanjut."},
    {"word": "一睡", "furigana": "いっすい", "romaji": "issui", "meaning": "Tidur sekejap mata", "level": "N1", "example": "心配で昨夜は一睡もできなかった。", "example_reading": "しんぱいでさくやはいっすいもできなかった。", "example_meaning": "Karena cemas semalam tidak bisa tidur sekejap pun."}
])

add_kanji(2, "嫌", "ケン、ゲン", "きら・う、いや", "Benci, enggan, suasana hati", [
    {"word": "機嫌", "furigana": "きげん", "romaji": "kigen", "meaning": "Suasana hati mood", "level": "N3", "example": "部長は朝からご機嫌だ。", "example_reading": "ぶちょうはあさからごきげんだ。", "example_meaning": "Bapak kepala manajer suasana hatinya sangat baik sejak pagi."},
    {"word": "嫌悪", "furigana": "けんお", "romaji": "ken'o", "meaning": "Rasa benci jijik muak", "level": "N1", "example": "不正行為に対して強い嫌悪感を抱く。", "example_reading": "ふせいこういにたいしてつよいけんおかんをいだく。", "example_meaning": "Menaruh rasa muak yang kuat terhadap tindak kecurangan."},
    {"word": "嫌気", "furigana": "いやけ", "romaji": "iyake", "meaning": "Rasa jenuh malas enggan", "level": "N1", "example": "単調な毎日に嫌気がさした。", "example_reading": "たんちょうなまいにちにいやけがさした。", "example_meaning": "Merasa jenuh muak dengan rutinitas sehari-hari yang monoton."},
    {"word": "嫌疑", "furigana": "けんぎ", "romaji": "kengi", "meaning": "Kecurigaan sangkaan pidana", "level": "N1", "example": "証拠不十分で嫌疑なしとされた。", "example_reading": "しょうこふじゅうぶんでけんぎなしとされた。", "example_meaning": "Dinyatakan bebas dari sangkaan karena kurangnya bukti."}
])

add_kanji(2, "署", "ショ", "", "Kantor dinas instansi, tanda tangan", [
    {"word": "警察署", "furigana": "けいさつしょ", "romaji": "keisatsusho", "meaning": "Kantor polisi", "level": "N3", "example": "落とし物を警察署に届けた。", "example_reading": "おとしものをけいさつしょにとどけた。", "example_meaning": "Melaporkan barang temuan ke kantor polisi."},
    {"word": "署名", "furigana": "しょめい", "romaji": "shomei", "meaning": "Tanda tangan tanda persetujuan", "level": "N2", "example": "契約書の最後に署名と捺印をする。", "example_reading": "けいやくしょのさいごにしょめいとなついんをする。", "example_meaning": "Membubuhkan tanda tangan dan cap stempel di akhir surat kontrak."},
    {"word": "消防署", "furigana": "しょうぼうしょ", "romaji": "shoubousho", "meaning": "Kantor pos pemadam kebakaran", "level": "N3", "example": "近所に新しい消防署ができた。", "example_reading": "きんじょにあたらしいしょうぼうしょができた。", "example_meaning": "Pos damkar baru didirikan di dekat rumah."},
    {"word": "部署", "furigana": "ぶしょ", "romaji": "busho", "meaning": "Divisi bagian penempatan tugas kantor", "level": "N2", "example": "新しい部署に配属された。", "example_reading": "あたらしいぶしょにはいぞくされた。", "example_meaning": "Ditempatkan di divisi departemen baru."}
])

add_kanji(2, "悔", "カイ", "く・いる、くや・しい", "Menyesal, kecewa", [
    {"word": "後悔", "furigana": "こうかい", "romaji": "koukai", "meaning": "Penyesalan di kemudian hari", "level": "N3", "example": "後悔しないように全力を尽くす。", "example_reading": "こうかいしないようにぜんりょくをつくす。", "example_meaning": "Berusaha sekuat tenaga agar tidak menyesal di kemudian hari."},
    {"word": "悔恨", "furigana": "かいこん", "romaji": "kaikon", "meaning": "Penyesalan mendalam rasa bersalah", "level": "N1", "example": "悔恨の涙を流した。", "example_reading": "かいこんのなみだをながした。", "example_meaning": "Meneteskan air mata penyesalan yang mendalam."},
    {"word": "悔悟", "furigana": "かいご", "romaji": "kaigo", "meaning": "Menyadari dosa dan bertaubat", "level": "N1", "example": "自らの過ちを悔悟する。", "example_reading": "みずからのあやまちをかいごする。", "example_meaning": "Bertaubat dan menyadari kesalahan masa lalunya sendiri."}
])

add_kanji(2, "隠", "イン", "かく・す、かく・れる", "Sembunyi, menyembunyikan", [
    {"word": "隠蔽", "furigana": "いんぺい", "romaji": "impei", "meaning": "Penyembunyian menutup-nutupi skandal kebenaran", "level": "N1", "example": "企業が事故の事実を隠蔽していた。", "example_reading": "きぎょうがじこのじじつをいんぺいしていた。", "example_meaning": "Perusahaan menutupi fakta insiden kecelakaan tersebut."},
    {"word": "隠居", "furigana": "いんきょ", "romaji": "inkyo", "meaning": "Pensiun menarik diri santai di hari tua", "level": "N1", "example": "仕事を引退して田舎で隠居生活を送る。", "example_reading": "しごとをいんたいしていなかでいんきょせいかつをおくる。", "example_meaning": "Pensiun dari pekerjaan dan menjalani masa tua santai di desa."},
    {"word": "隠語", "furigana": "いんご", "romaji": "ingo", "meaning": "Bahasa sandi kode rahasia / slang kelompok", "level": "N1", "example": "仲間内だけで通じる隠語を使う。", "example_reading": "なかまうちだけでつうじるいんごをつかう。", "example_meaning": "Menggunakan bahasa sandi rahasia yang hanya dimengerti kalangan sendiri."}
])

# ==========================================
# MINGGU 3 (28 Kanji)
# 褒、謙、遜、担、脇、脚、脈、偉、徐、弊、老、舗、絨、毯、拓、鼓、鬼、棋、寿、嬢、欧、揺、環、境、誉、徳、怠、駄
# ==========================================
add_kanji(3, "褒", "ホウ", "ほ・める", "Memuji, menghadiahi, sanjungan", [
    {"word": "褒美", "furigana": "ほうび", "romaji": "houbi", "meaning": "Hadiah ganjaran atas prestasi jerih payah", "level": "N2", "example": "試験に合格したご褒美に時計をもらった。", "example_reading": "しけんにごうかくしたごほうびにとけいをもらった。", "example_meaning": "Mendapat hadiah jam tangan sebagai ganjaran lulus ujian."},
    {"word": "褒賞", "furigana": "ほうしょう", "romaji": "houshou", "meaning": "Penghargaan medali kehormatan", "level": "N1", "example": "長年の功績に対して褒賞が授与された。", "example_reading": "ながねんのこうせきにたいしてほうしょうがじゅよされた。", "example_meaning": "Penghargaan dianugerahkan atas jasa pengabdian bertahun-tahun."},
    {"word": "賛褒", "furigana": "さんぽう", "romaji": "sampou", "meaning": "Pujian sanjungan kagum", "level": "N1", "example": "彼の勇気ある行動に賛褒の声が集まった。", "example_reading": "かれのゆうきあるこうどうにさんぽうのこえがあつまった。", "example_meaning": "Tindakan beraninya menuai sanjungan pujian dari khalayak."}
])

add_kanji(3, "謙", "ケン", "", "Rendah hati, santun tawadhu", [
    {"word": "謙虚", "furigana": "けんきょ", "romaji": "kenkyo", "meaning": "Rendah hati / tidak sombong tawadhu", "level": "N2", "example": "成功しても常に謙虚な姿勢を忘れない。", "example_reading": "せいこうしてもつねにけんきょなしせいをわすれない。", "example_meaning": "Bahkan ketika sukses, selalu tidak melupakan sikap rendah hati."},
    {"word": "謙遜", "furigana": "けんそん", "romaji": "kenson", "meaning": "Kerendahan hati merendah", "level": "N2", "example": "褒められて謙遜する。", "example_reading": "ほめられてけんそんする。", "example_meaning": "Merendah ketika dipuji orang lain."},
    {"word": "謙譲", "furigana": "けんじょう", "romaji": "kenjou", "meaning": "Sopan santun merendahkan diri (kenjougo)", "level": "N1", "example": "ビジネスで謙譲語を正しく使い分ける。", "example_reading": "びじねすでけんじょうごをただしくつかいわける。", "example_meaning": "Menggunakan tata bahasa sopan merendah (kenjougo) dengan tepat dalam bisnis."}
])

add_kanji(3, "遜", "ソン", "へりくだ・る", "Kalah saing, merendah", [
    {"word": "謙遜", "furigana": "けんそん", "romaji": "kenson", "meaning": "Kerendahan hati merendah", "level": "N2", "example": "そんなに謙遜しなくても大丈夫ですよ。", "example_reading": "そんなにけんそんしなくてもだいじょうぶですよ。", "example_meaning": "Anda tidak perlu merendah hati berlebihan seperti itu kok."},
    {"word": "遜色", "furigana": "そんしょく", "romaji": "sonshoku", "meaning": "Kalah saing / inferior (biasa: 遜色ない = tak kalah saing)", "level": "N1", "example": "プロの作品と比べても遜色がない。", "example_reading": "ぷろのさくひんとくらべてもそんしょくがない。", "example_meaning": "Bahkan dibandingkan dengan karya profesional pun tak kalah saing sama sekali."}
])

add_kanji(3, "担", "タン", "かつ・ぐ、にな・う", "Memikul, menanggung beban tugas", [
    {"word": "担当", "furigana": "たんとう", "romaji": "tantou", "meaning": "Penanggung jawab bertugas", "level": "N3", "example": "このプロジェクトを担当しています。", "example_reading": "このぷろじぇくとをたんとうしています。", "example_meaning": "Saya yang bertanggung jawab mengurusi proyek ini."},
    {"word": "負担", "furigana": "ふたん", "romaji": "futan", "meaning": "Beban tanggungan biaya kerja", "level": "N2", "example": "費用は会社が全額負担します。", "example_reading": "ひようはかいしゃがぜんがくふたんします。", "example_meaning": "Biaya ditanggung sepenuhnya oleh kantor perusahaan."},
    {"word": "分担", "furigana": "ぶんたん", "romaji": "buntan", "meaning": "Pembagian tugas porsi kerja", "level": "N2", "example": "家事を家族みんなで分担する。", "example_reading": "かじをかぞくみんなでぶんたんする。", "example_meaning": "Membagi tugas pekerjaan rumah bersama seluruh keluarga."},
    {"word": "担架", "furigana": "たんか", "romaji": "tanka", "meaning": "Tandu medis pasien darurat", "level": "N1", "example": "負傷者を担架で救急車へ運ぶ。", "example_reading": "ふしょうしゃをたんかできゅうきゅうしゃへはこぶ。", "example_meaning": "Membawa korban luka menggunakan tandu ke ambulans."}
])

add_kanji(3, "脇", "キョウ", "わき", "Ketiak, sisi samping, peran pendukung", [
    {"word": "脇役", "furigana": "わきやく", "romaji": "wakiyaku", "meaning": "Peran pendukung / tokoh sampingan", "level": "N1", "example": "名脇役としてドラマを盛り上げる。", "example_reading": "めいわきやくとしてどらまをもりあげる。", "example_meaning": "Menghidupkan drama sebagai aktor pemeran pendukung kawakan."},
    {"word": "脇道", "furigana": "わきみち", "romaji": "wakimichi", "meaning": "Jalan pintas samping / gang kecil", "level": "N2", "example": "大通りを避けて脇道を通る。", "example_reading": "おおどおりをさけてわきみちをとおる。", "example_meaning": "Menghindari jalan raya besar dan lewat jalan samping."},
    {"word": "脇見", "furigana": "わきみ", "romaji": "wakimi", "meaning": "Meleng / menoleh ke samping saat jalan/setir", "level": "N1", "example": "脇見運転は重大な事故の原因になる。", "example_reading": "わきみうんてんはじゅうだいなじこのげんいんになる。", "example_meaning": "Menyetir sambil meleng menoleh bisa menjadi pemicu kecelakaan fatal."}
])

add_kanji(3, "脚", "キャク、キャ", "あし", "Kaki tumpuan, naskah drama", [
    {"word": "脚本", "furigana": "きゃくほん", "romaji": "kyakuhon", "meaning": "Naskah skenario drama/film", "level": "N2", "example": "映画の脚本を半年かけて書き上げた。", "example_reading": "えいがのきゃくほんをはんリンクかけてかきあげた。", "example_meaning": "Menyelesaikan penulisan naskah skenario film selama setengah tahun."},
    {"word": "三脚", "furigana": "さんきゃく", "romaji": "sankyaku", "meaning": "Tripod kaki tiga", "level": "N2", "example": "カメラを三脚に固定して撮影する。", "example_reading": "かめらをさんきゃくにこていしてさつえいする。", "example_meaning": "Memasang kamera di atas tripod lalu memotret."},
    {"word": "脚色", "furigana": "きゃくしょく", "romaji": "kyakushoku", "meaning": "Dramatisasi adaptasi cerita", "level": "N1", "example": "実話を脚色して小説にした。", "example_reading": "じつわをきゃくしょくしてしょうせつにした。", "example_meaning": "Mengadaptasi kisah nyata menjadi sebuah novel."},
    {"word": "失脚", "furigana": "しっきゃく", "romaji": "shikkyaku", "meaning": "Jatuh lengser dari jabatan kuasa", "level": "N1", "example": "スキャンダルで失脚した。", "example_reading": "すきゃんだるでしっきゃくした。", "example_meaning": "Lengser jatuh dari jabatan karena skandal."}
])

add_kanji(3, "脈", "ミャク", "", "Nadi denyut, koneksi relasi, urat", [
    {"word": "脈拍", "furigana": "みゃくはく", "romaji": "myakuhaku", "meaning": "Denyut nadi", "level": "N2", "example": "運動後に脈拍を測る。", "example_reading": "うんどうごにみゃくはくをはかる。", "example_meaning": "Mengukur denyut nadi setelah berolahraga."},
    {"word": "人脈", "furigana": "じんみゃく", "romaji": "jimmyaku", "meaning": "Jaringan koneksi relasi pertemanan kerja", "level": "N1", "example": "仕事で幅広い人脈を築いた。", "example_reading": "しごとではばひろいじんみゃくをきずいた。", "example_meaning": "Membangun jaringan relasi koneksi yang luas dalam pekerjaan."},
    {"word": "文脈", "furigana": "ぶんみゃく", "romaji": "bummyaku", "meaning": "Konteks kalimat", "level": "N1", "example": "前後の文脈から意味を推測する。", "example_reading": "ぜんごのぶんみゃくからいみをすいそくする。", "example_meaning": "Menebak arti kata dari konteks kalimat sebelum dan sesudahnya."},
    {"word": "動脈", "furigana": "どうみゃく", "romaji": "doumyaku", "meaning": "Pembuluh darah arteri", "level": "N1", "example": "動脈硬化を予防する食生活を心がける。", "example_reading": "どうみゃくこうかをよぼうするしょくせいかつをこころがける。", "example_meaning": "Menjaga pola makan untuk mencegah pengerasan arteri."}
])

add_kanji(3, "偉", "イ", "えら・い", "Agung, hebat, luar biasa", [
    {"word": "偉大", "furigana": "いだい", "romaji": "idai", "meaning": "Agung luar biasa akbar", "level": "N2", "example": "歴史上の偉大な指導者を称える。", "example_reading": "れきしじょうのいだいなしどうしゃをたたえる。", "example_meaning": "Memuji memuliakan pemimpin agung dalam sejarah."},
    {"word": "偉人", "furigana": "いじん", "romaji": "ijin", "meaning": "Tokoh besar agung pahlawan sejarah", "level": "N2", "example": "子供の頃に偉人の伝記を読んだ。", "example_reading": "こどものころにいじんのでんきをよんだ。", "example_meaning": "Membaca biografi tokoh-tokoh besar dunia di masa kecil."},
    {"word": "偉業", "furigana": "いぎょう", "romaji": "igyou", "meaning": "Pencapaian prestasi gemilang monumental", "level": "N1", "example": "前人未到の偉業を達成した。", "example_reading": "ぜんじんみとうのいぎょうをたっせいした。", "example_meaning": "Meraih prestasi gemilang yang belum pernah dicapai siapapun sebelumnya."}
])

add_kanji(3, "徐", "ジョ", "おもむろ・に", "Perlahan lambat pelan", [
    {"word": "徐行", "furigana": "じょこう", "romaji": "jokou", "meaning": "Melaju perlahan pelan-pelan (rambu jalan)", "level": "N1", "example": "学校の周辺では車を徐行させる。", "example_reading": "がっこうのしゅうへんではくるまをじょこうさせる。", "example_meaning": "Menjalankan mobil secara perlahan di area sekitar sekolah."},
    {"word": "徐々", "furigana": "じょじょ", "romaji": "jojo", "meaning": "Lambat laun sedikit demi sedikit bertahap", "level": "N3", "example": "病状が徐々に良くなってきた。", "example_reading": "びょうじょうがじょじょによくなってきた。", "example_meaning": "Kondisi penyakitnya lambat laun mulai membaik."}
])

add_kanji(3, "弊", "ヘイ", "", "Buruk, dampak jelek, sebutan rendah diri kami", [
    {"word": "弊社", "furigana": "へいしゃ", "romaji": "heisha", "meaning": "Perusahaan kami (bahasa sopan rendah diri)", "level": "N2", "example": "弊社をご利用いただき誠にありがとうございます。", "example_reading": "へいしゃをごりよういただきまことにありがとうございます。", "example_meaning": "Terima kasih banyak telah menggunakan jasa perusahaan kami."},
    {"word": "弊害", "furigana": "へいがい", "romaji": "heigai", "meaning": "Dampak buruk efek samping negatif", "level": "N1", "example": "スマートフォンの使いすぎによる弊害を考える。", "example_reading": "すまーとふぉんのつかいすぎによるへいがいをかんがえる。", "example_meaning": "Memikirkan dampak negatif dari penggunaan smartphone berlebihan."},
    {"word": "疲弊", "furigana": "ひへい", "romaji": "hihei", "meaning": "Keletihan terkuras fisik finansial lesu", "level": "N1", "example": "長引く不況で地方経済が疲弊している。", "example_reading": "ながびくふきょうでちほうけいざいがひへいしている。", "example_meaning": "Ekonomi daerah lesu terpuruk akibat resesi yang berlarut-larut."},
    {"word": "悪弊", "furigana": "あくへい", "romaji": "akuhei", "meaning": "Kebiasaan adat buruk tradisi korup", "level": "N1", "example": "古い組織の悪弊を断ち切る。", "example_reading": "ふるいそしきのあくへいをたちきる。", "example_meaning": "Memutus kebiasaan buruk tradisi lama organisasi."}
])

add_kanji(3, "老", "ロウ", "お・いる、ふ・ける", "Tua, lanjut usia, berpengalaman", [
    {"word": "老人", "furigana": "ろうじん", "romaji": "roujin", "meaning": "Lansia kakek nenek orang tua", "level": "N3", "example": "電車でお年寄りに席を譲った。", "example_reading": "でんしゃでおとしよりにせきをゆずった。", "example_meaning": "Memberikan kursi prioritas kepada orang tua di kereta."},
    {"word": "老化", "furigana": "ろうか", "romaji": "rouka", "meaning": "Penuaan proses menjadi tua", "level": "N2", "example": "適度な運動が老化防止に役立つ。", "example_reading": "てきどなうんどうがろうかぼうしにやくだつ。", "example_meaning": "Olahraga teratur bermanfaat mencegah penuaan dini."},
    {"word": "老後", "furigana": "ろうご", "romaji": "rougo", "meaning": "Masa hari tua pensiun", "level": "N2", "example": "老後の生活資金を準備する。", "example_reading": "ろうごのせいかつしきんをじゅんびする。", "example_meaning": "Mempersiapkan tabungan dana hidup untuk masa hari tua."},
    {"word": "老若男女", "furigana": "ろうにゃくなんにょ", "romaji": "rounyakunannyo", "meaning": "Tua muda pria wanita segenap khalayak", "level": "N1", "example": "老若男女を問わず楽しめるイベントだ。", "example_reading": "ろうにゃくなんにょをとわずたのしめるいべんとだ。", "example_meaning": "Acara yang bisa dinikmati siapa saja tanpa memandang tua-muda pria-wanita."}
])

add_kanji(3, "舗", "ホ", "", "Toko kedai gerai", [
    {"word": "店舗", "furigana": "てんぽ", "romaji": "tempo", "meaning": "Toko fisik gerai cabang outlet", "level": "N2", "example": "全国に百店舗を展開している。", "example_reading": "ぜんこくにひゃくてんぽをてんかいしている。", "example_meaning": "Membuka ekspansi 100 gerai toko di seantero negeri."},
    {"word": "老舗", "furigana": "しにせ", "romaji": "shinise", "meaning": "Toko lawas legendaris berumur ratusan tahun", "level": "N1", "example": "京都の老舗和菓子店でお土産を買った。", "example_reading": "きょうとのしにせわがしてんでおみやげをかった。", "example_meaning": "Membeli oleh-oleh di toko kue tradisional legendaris di Kyoto."},
    {"word": "本舗", "furigana": "ほんぽ", "romaji": "hompo", "meaning": "Toko pusat orisinal produsen utama", "level": "N1", "example": "創業百年の本舗の味を守る。", "example_reading": "そうぎょうひゃくねんのほんぽのあじをまもる。", "example_meaning": "Menjaga keaslian cita rasa toko pusat legendaris berusia seabad."},
    {"word": "舗装", "furigana": "ほそう", "romaji": "hosou", "meaning": "Pengaspalan perkerasan jalan", "level": "N1", "example": "道路がきれいに舗装された。", "example_reading": "どうろがきれいにほそうされた。", "example_meaning": "Jalan raya sudah diaspal dengan rapi."}
])

add_kanji(3, "絨", "ジュウ", "", "Bulu karpet tebal permadani", [
    {"word": "絨毯", "furigana": "じゅうたん", "romaji": "juutan", "meaning": "Karpet tebal permadani lantai", "level": "N2", "example": "居間にペルシャ絨毯を敷いた。", "example_reading": "いまにぺるしゃじゅうたんをしいた。", "example_meaning": "Menggelar karpet permadani Persia di ruang keluarga."},
    {"word": "絨毛", "furigana": "じゅうもう", "romaji": "juumou", "meaning": "Bulu vili halus pada permukaan", "level": "N1", "example": "小腸の絨毛から栄養が吸収される。", "example_reading": "しょうちょうのじゅうもうからえいようがきゅうしゅうされる。", "example_meaning": "Nutrisi diserap melalui vili (bulu halus) usus halus."}
])

add_kanji(3, "毯", "タン", "", "Permadani selimut wol kain tebal", [
    {"word": "絨毯", "furigana": "じゅうたん", "romaji": "juutan", "meaning": "Karpet tebal permadani", "level": "N2", "example": "汚れた絨毯をクリーニングに出す。", "example_reading": "よごれたじゅうたんをくりーにんぐにだす。", "example_meaning": "Membawa karpet yang kotor ke penatu (laundry)."},
    {"word": "毛毯", "furigana": "もうたん", "romaji": "moutan", "meaning": "Selimut wol hangat permadani tebal", "level": "N1", "example": "毛毯をかぶって暖をとる。", "example_reading": "もうたんをかぶってだんをとる。", "example_meaning": "Menyelimuti diri dengan selimut wol untuk menghangatkan badan."}
])

add_kanji(3, "拓", "タク", "", "Membuka lahan baru, merintis", [
    {"word": "開拓", "furigana": "かいたく", "romaji": "kaitaku", "meaning": "Perintisan pembukaan lahan baru jalur baru", "level": "N1", "example": "海外市場を開拓する計画だ。", "example_reading": "かいがいしじょうをかいたくするけいかくだ。", "example_meaning": "Rencana untuk merintis membuka pasar luar negeri."},
    {"word": "拓殖", "furigana": "たくしょく", "romaji": "takushoku", "meaning": "Pengembangan wilayah pembukaan lahan koloni", "level": "N1", "example": "拓殖大学で国際関係を学ぶ。", "example_reading": "たくしょくだいがくでこくさいかんけいをまなぶ。", "example_meaning": "Belajar hubungan internasional di Universitas Takushoku."},
    {"word": "魚拓", "furigana": "ぎょたく", "romaji": "gyotaku", "meaning": "Gyotaku (cetakan tinta tubuh ikan hasil pancing)", "level": "Umum", "example": "大物を釣り上げて魚拓を取った。", "example_reading": "おおものをつりあげてぎょたくをとった。", "example_meaning": "Memancing ikan raksasa lalu membuat cetakan gyotaku sebagai kenangan."}
])

add_kanji(3, "鼓", "コ", "つづみ", "Drum kendang taiko, menggetarkan", [
    {"word": "太鼓", "furigana": "たいこ", "romaji": "taiko", "meaning": "Drum taiko Jepang gendang", "level": "N2", "example": "夏祭りで和太鼓の演奏を聞いた。", "example_reading": "なつまつりでわだいこのえんそうをきいた。", "example_meaning": "Mendengarkan tabuhan drum wadaiko di festival musim panas."},
    {"word": "鼓動", "furigana": "こどう", "romaji": "kodou", "meaning": "Denyut debaran detak jantung", "level": "N1", "example": "緊張で心臓の鼓動が速くなった。", "example_reading": "きんちょうでしんぞうのこどうがはやくなった。", "example_meaning": "Detak debar jantung berdegup kencang karena tegang."},
    {"word": "鼓舞", "furigana": "こぶ", "romaji": "kobu", "meaning": "Menyemangati mengobarkan kobaran semangat", "level": "N1", "example": "監督の熱い言葉が選手たちを鼓舞した。", "example_reading": "かんとくのあついことばがせんしゅたちをこぶした。", "example_meaning": "Kata-kata penuh semangat pelatih mengobarkan semangat para pemain."},
    {"word": "鼓膜", "furigana": "こまく", "romaji": "komaku", "meaning": "Gendang telinga pendengaran", "level": "N1", "example": "大音量で鼓膜が破れそうだった。", "example_reading": "だいおんりょうでこまくがやぶれそうだった。", "example_meaning": "Gendang telinga rasanya nyaris pecah karena suara yang teramat keras."}
])

add_kanji(3, "鬼", "キ", "おに", "Iblis ogre iblis setan hantu", [
    {"word": "鬼才", "furigana": "きさい", "romaji": "kisai", "meaning": "Jenius luar biasa bertalenta langka", "level": "N1", "example": "映画界の鬼才と呼ばれる監督だ。", "example_reading": "えいがかいのきさいとよばれるかんとくだ。", "example_meaning": "Sutradara yang dijuluki jenius luar biasa dalam dunia perfilman."},
    {"word": "悪鬼", "furigana": "あっき", "romaji": "akki", "meaning": "Iblis jahat setan bengis", "level": "N1", "example": "悪鬼のごとき形相で怒鳴りつけた。", "example_reading": "あっきのごときぎょうそうでどなりつけた。", "example_meaning": "Membentak teriak dengan ekspresi muka bengis bak iblis jahat."},
    {"word": "疑心暗鬼", "furigana": "ぎしんあんき", "romaji": "gishin'anki", "meaning": "Curiga berlebihan membabi buta", "level": "N1", "example": "疑心暗鬼になって味方まで疑ってしまう。", "example_meaning": "Karena curiga berlebihan, kawan sendiri pun ikut dicurigai.", "example_reading": "ぎしんあんきになってみかたまでうたがってしまう。"},
    {"word": "鬼ごっこ", "furigana": "おにごっこ", "romaji": "onigokko", "meaning": "Permainan kejar-kejaran anak", "level": "Umum", "example": "公園で子供たちが鬼ごっこをしている。", "example_reading": "こうえんでこどもたちがおにごっこをしている。", "example_meaning": "Anak-anak bermain kejar-kejaran di taman."}
])

add_kanji(3, "棋", "キ", "", "Papan catur, shogi catur Jepang", [
    {"word": "将棋", "furigana": "しょうぎ", "romaji": "shougi", "meaning": "Shogi (catur tradisional Jepang)", "level": "N3", "example": "祖父と将棋を指すのが日課だ。", "example_reading": "そふとしょうぎをさすのがにっかだ。", "example_meaning": "Bermain catur shogi bersama kakek adalah rutinitas harian saya."},
    {"word": "棋士", "furigana": "きし", "romaji": "kishi", "meaning": "Pemain master catur profesional", "level": "N1", "example": "プロ棋士の対局をネットで観戦する。", "example_reading": "ぷろきしのたいきょくをねっとでかんせんする。", "example_meaning": "Menonton pertandingan pemain master catur profesional lewat internet."},
    {"word": "棋譜", "furigana": "きふ", "romaji": "kifu", "meaning": "Catatan notasi langkah permainan catur", "level": "N1", "example": "名人の棋譜を並べて勉強する。", "example_reading": "めいじんのきふをならべてべんきょうする。", "example_meaning": "Belajar dengan menelusuri catatan langkah master catur."}
])

add_kanji(3, "寿", "ジュ", "ことぶき", "Umur panjang, selamat berkah", [
    {"word": "寿命", "furigana": "じゅみょう", "romaji": "jumyou", "meaning": "Masa hidup usia / masa pakai alat", "level": "N2", "example": "日本人の平均寿命が延びている。", "example_reading": "にほんじんのへいきんじゅみょうがのびている。", "example_meaning": "Rata-rata angka harapan hidup orang Jepang terus meningkat."},
    {"word": "長寿", "furigana": "ちょうじゅ", "romaji": "chouju", "meaning": "Panjang umur", "level": "N2", "example": "祖母の長寿をお祝いした。", "example_reading": "そぼのちょうじゅをおいわいした。", "example_meaning": "Merayakan panjang umur nenek tercinta."},
    {"word": "寿司", "furigana": "すし", "romaji": "sushi", "meaning": "Sushi hidangan nasi kepal Jepang", "level": "N4", "example": "回転寿司でマグロを食べた。", "example_reading": "かいてんずしでまぐろをたべた。", "example_meaning": "Makan ikan tuna di restoran sushi ban berjalan."},
    {"word": "慶寿", "furigana": "けいじゅ", "romaji": "keiju", "meaning": "Perayaan berkah usia lanjut", "level": "N1", "example": "慶寿の祝宴が開かれた。", "example_reading": "けいじゅのしゅくえんがひらかれた。", "example_meaning": "Pesta jamuan perayaan usia lanjut diadakan."}
])

add_kanji(3, "嬢", "ジョウ", "", "Putri gadis muda nona", [
    {"word": "お嬢さん", "furigana": "おじょうさん", "romaji": "ojousan", "meaning": "Gadis muda nona / putri seseorang", "level": "N3", "example": "お嬢さんは今年おいくつですか。", "example_reading": "おじょうさんはことしおいくつですか。", "example_meaning": "Putri Anda tahun ini berusia berapa tahun?"},
    {"word": "令嬢", "furigana": "れいじょう", "romaji": "reijou", "meaning": "Putri bangsawan ningrat / putri terhormat", "level": "N1", "example": "社長のご令嬢と結婚することになった。", "example_reading": "しゃちょうのごれいじょうとけっこんすることになった。", "example_meaning": "Diputuskan menikah dengan putri tuan direktur."},
    {"word": "愛嬢", "furigana": "あいじょう", "romaji": "aijou", "meaning": "Putri kesayangan tercinta", "level": "N1", "example": "愛嬢の結婚式で父親が涙を浮かべた。", "example_reading": "あいじょうのけっこんしきでちちおやがなみだをうかべた。", "example_meaning": "Sang ayah meneteskan air mata di pesta pernikahan putri tercintanya."}
])

add_kanji(3, "欧", "オウ", "", "Eropa barat", [
    {"word": "欧米", "furigana": "おうべい", "romaji": "oubei", "meaning": "Negara Barat (Eropa dan Amerika)", "level": "N3", "example": "欧米の文化と日本の文化を比較する。", "example_reading": "おうべいのぶんかにほんのぶんかをひかくする。", "example_meaning": "Membandingkan kebudayaan Barat dan kebudayaan Jepang."},
    {"word": "欧州", "furigana": "おうしゅう", "romaji": "oushuu", "meaning": "Benua Eropa", "level": "N2", "example": "欧州連合（EU）の加盟国だ。", "example_reading": "おうしゅうれんごうのかめいこくだ。", "example_meaning": "Merupakan negara anggota Uni Eropa (EU)."},
    {"word": "西欧", "furigana": "せいおう", "romaji": "seiou", "meaning": "Eropa Barat", "level": "N2", "example": "西欧諸国への旅行を計画している。", "example_reading": "せいおうしょこくへのりょこうをけいかくしている。", "example_meaning": "Merencanakan liburan wisata ke negara-negara Eropa Barat."},
    {"word": "東欧", "furigana": "とうおう", "romaji": "touou", "meaning": "Eropa Timur", "level": "N2", "example": "東欧の民族音楽を聴く。", "example_reading": "とうおうのみんぞくおんがくをきく。", "example_meaning": "Mendengarkan musik tradisional rakyat Eropa Timur."}
])

add_kanji(3, "揺", "ヨウ", "ゆ・れる、ゆ・る", "Goyang getar berayun goncang", [
    {"word": "動揺", "furigana": "どうよう", "romaji": "douyou", "meaning": "Goncangan emosi jiwa / gelisah resah", "level": "N1", "example": "突然の知らせに動揺を隠せない。", "example_reading": "とつぜんのしらせにどうようをかくせない。", "example_meaning": "Tak mampu menyembunyikan kegelisahan akibat kabar mendadak."},
    {"word": "揺籃", "furigana": "ようらん", "romaji": "youran", "meaning": "Buaian ayunan bayi / tempat kelahiran awal", "level": "N1", "example": "この町は近代産業の揺籃の地だ。", "example_reading": "このまちはきんだいさんぎょうのようらんのちだ。", "example_meaning": "Kota ini adalah buaian tempat lahirnya industri modern."},
    {"word": "揺動", "furigana": "ようどう", "romaji": "youdou", "meaning": "Getaran bergoyang oscilasi fisik", "level": "N1", "example": "地震による建物の揺動を測定する。", "example_reading": "じしんによるたてもののようどうをそくていする。", "example_meaning": "Mengukur goyangan gedung akibat gempa bumi."}
])

add_kanji(3, "環", "カン", "わ", "Lingkaran gelang, keliling, lingkungan", [
    {"word": "環境", "furigana": "かんきょう", "romaji": "kankyou", "meaning": "Lingkungan hidup alam sekitar", "level": "N3", "example": "地球環境を守るために節電する。", "example_reading": "ちきゅうかんきょうをまもるためにせつでんする。", "example_meaning": "Menghemat listrik demi menjaga lingkungan bumi."},
    {"word": "循環", "furigana": "じゅんかん", "romaji": "junkan", "meaning": "Sirkulasi peredaran perputaran", "level": "N2", "example": "血液の循環を良くするマッサージ。", "example_reading": "けつえきのじゅんかんをよくするまっさーじ。", "example_meaning": "Pijat untuk melancarkan sirkulasi peredaran darah."},
    {"word": "連環", "furigana": "れんかん", "romaji": "renkan", "meaning": "Kaitan mata rantai saling terhubung", "level": "N1", "example": "因果の連環を解き明かす。", "example_reading": "いんがのれんかんをときあかす。", "example_meaning": "Mengungkap mata rantai sebab akibat."},
    {"word": "環状", "furigana": "かんじょう", "romaji": "kanjou", "meaning": "Bentuk lingkaran cincin (jalan lingkar)", "level": "N1", "example": "都心を結ぶ環状線を走る。", "example_reading": "としんをむすぶかんじょうせんをはしる。", "example_meaning": "Melaju di jalur jalan tol lingkar lingkar kota."}
])

add_kanji(3, "境", "キョウ、ケイ", "さかい", "Batas perbatasan lingkungan kondisi", [
    {"word": "国境", "furigana": "こっきょう", "romaji": "kokkyou", "meaning": "Perbatasan antar negara", "level": "N3", "example": "列車で国境を越えた。", "example_reading": "れっしゃでこっきょうをこえた。", "example_meaning": "Melintasi batas antar negara dengan kereta api."},
    {"word": "境遇", "furigana": "きょうぐう", "romaji": "kyouguu", "meaning": "Nasib kondisi lingkungan hidup seseorang", "level": "N1", "example": "似たような境遇の友人と語り合う。", "example_reading": "にたようなきょうぐうのゆうじんとかたりあう。", "example_meaning": "Berbincang bertukar cerita dengan teman yang bernasib serupa."},
    {"word": "心境", "furigana": "しんきょう", "romaji": "shinkyou", "meaning": "Kondisi suasana batin isi hati", "level": "N1", "example": "転職を決めた現在の心境を語る。", "example_reading": "てんしょくをきめたげんざいのしんきょうをかたる。", "example_meaning": "Menceritakan kondisi suasana batin saat memutuskan pindah kerja."},
    {"word": "境界", "furigana": "きょうかい", "romaji": "kyoukai", "meaning": "Batas sekat perbatasan pembatas", "level": "N2", "example": "土地の境界線を明確にする。", "example_reading": "とちのきょうかいせんをめいかくにする。", "example_meaning": "Memperjelas garis batas kepemilikan tanah."}
])

add_kanji(3, "誉", "ヨ", "ほま・れ", "Kehormatan nama baik reputasi", [
    {"word": "名誉", "furigana": "めいよ", "romaji": "meiyo", "meaning": "Kehormatan reputasi nama baik", "level": "N1", "example": "名誉ある賞を受賞した。", "example_reading": "めいよあるしょうをじゅしょうした。", "example_meaning": "Menerima penghargaan yang sangat terhormat."},
    {"word": "栄誉", "furigana": "えいよ", "romaji": "eiyo", "meaning": "Kemuliaan kehormatan prestisius", "level": "N1", "example": "国民栄誉賞が授与された。", "example_reading": "こくみんえいよしょうがじゅよされた。", "example_meaning": "Penghargaan Kehormatan Rakyat Nasional dianugerahkan."},
    {"word": "毀誉", "furigana": "きよ", "romaji": "kiyo", "meaning": "Cacian dan pujian penilaian orang", "level": "N1", "example": "世間の毀誉褒貶に惑わされない。", "example_reading": "せけんのきよほうへんにまどわされない。", "example_meaning": "Tidak terombang-ambing oleh cacian maupun pujian publik."}
])

add_kanji(3, "徳", "トク", "", "Moralitas kebajikan budi pekerti", [
    {"word": "道徳", "furigana": "どうとく", "romaji": "doutoku", "meaning": "Moralitas budi pekerti norma etika", "level": "N2", "example": "道徳的な判断が求められる場面だ。", "example_reading": "どうとくてきなはんだんがもとめられるばめんだ。", "example_meaning": "Situasi yang menuntut penilaian berdasarkan moralitas budi pekerti."},
    {"word": "美徳", "furigana": "びとく", "romaji": "bitoku", "meaning": "Kebajikan luhur kebaikan mulia", "level": "N1", "example": "謙虚さは日本の伝統的な美徳とされる。", "example_reading": "けんきょさはにほんのでんとうてきなびとくとされる。", "example_meaning": "Sikap rendah hati dianggap sebagai kebajikan luhur tradisional Jepang."},
    {"word": "人徳", "furigana": "じんとく", "romaji": "jintoku", "meaning": "Kharisma budi luhur disegani orang", "level": "N1", "example": "彼の人徳を慕って多くの仲間が集まる。", "example_reading": "かれのじんとくをしたっておおくのなかまがあつまる。", "example_meaning": "Banyak rekan berkumpul karena kagum akan keluhuran budinya."},
    {"word": "恩徳", "furigana": "おんどく", "romaji": "ondoku", "meaning": "Kebaikan budi jasa pertolongan", "level": "N1", "example": "師匠の恩徳に深く感謝する。", "example_reading": "ししょうのおんどくにふかくかんしゃする。", "example_meaning": "Bersyukur sangat berterima kasih atas kebaikan jasa sang guru."}
])

add_kanji(3, "怠", "タイ", "おこた・る、なま・ける", "Malas lalai mengabaikan tugas", [
    {"word": "怠慢", "furigana": "たいまん", "romaji": "taiman", "meaning": "Kelalaian pengabaian tugas teledor", "level": "N1", "example": "職務怠慢で処分を受けた。", "example_reading": "しょくむたいまんでしょぶんをうけた。", "example_meaning": "Diberi sanksi hukuman karena kelalaian dalam tugas kerja."},
    {"word": "怠惰", "furigana": "たいだ", "romaji": "taida", "meaning": "Kemalasan pemalas tidak mau gerak", "level": "N1", "example": "怠惰な生活習慣を改善する。", "example_reading": "たいだなせいかつしゅうかんをかいぜんする。", "example_meaning": "Memperbaiki pola kebiasaan hidup yang serba malas."},
    {"word": "倦怠", "furigana": "けんたい", "romaji": "kentai", "meaning": "Rasa jenuh lesu letih", "level": "N1", "example": "全身に強い倦怠感を感じる。", "example_reading": "ぜんしんにつよいけんたいかんをかんじる。", "example_meaning": "Merasakan rasa lesu letih yang berat di sekujur tubuh."}
])

add_kanji(3, "駄", "ダ", "", "Sia-sia mubazir beban", [
    {"word": "無駄", "furigana": "むだ", "romaji": "muda", "meaning": "Sia-sia mubazir buang-buang waktu/uang", "level": "N3", "example": "時間を無駄に過ごしてはいけない。", "example_reading": "じかんをむだにすごしてはいけない。", "example_meaning": "Tidak boleh menghabiskan waktu secara sia-sia."},
    {"word": "駄作", "furigana": "ださく", "romaji": "dasaku", "meaning": "Karya buruk karya jelek gagal", "level": "N1", "example": "期待していた映画だが、駄作だった。", "example_reading": "きたいしていたえいがだが、ださくだった。", "example_meaning": "Film yang dinanti-nanti tapi ternyata karya gagal."},
    {"word": "駄菓子", "furigana": "だがし", "romaji": "dagashi", "meaning": "Jajanan pasar murah jajanan masa kecil", "level": "N2", "example": "駄菓子屋で懐かしいお菓子を買った。", "example_reading": "だがしやでなつかしいおかしをかった。", "example_meaning": "Membeli camilan bernostalgia di warung jajanan rakyat."},
    {"word": "下駄", "furigana": "げた", "romaji": "geta", "meaning": "Bakiak kayu tradisional Jepang", "level": "N2", "example": "浴衣を着て下駄を鳴らして歩く。", "example_reading": "ゆかたをきてげたをならしてあるく。", "example_meaning": "Mengenakan yukata dan berjalan dengan gemeretak bakiak kayu geta."}
])

# ==========================================
# MINGGU 4 (15 Kanji Unik)
# 慰、漏、盗、厳、遺、振、励、折、鍵、骨、津、尋、燃、蔵、創 (user wrote 盗 twice)
# ==========================================
add_kanji(4, "慰", "イ", "なぐさ・める", "Menghibur menenangkan pelipur lara", [
    {"word": "慰謝料", "furigana": "いしゃりょう", "romaji": "isharyou", "meaning": "Uang ganti rugi imateriil / kompensasi santunan", "level": "N1", "example": "離婚に伴う慰謝料を請求する。", "example_reading": "りこんにともなういしゃりょうをせいきゅうする。", "example_meaning": "Menuntut uang ganti rugi imateriil atas perceraian."},
    {"word": "慰問", "furigana": "いもん", "romaji": "imon", "meaning": "Kunjungan simpati penghiburan korban/pasien", "level": "N1", "example": "被災地へ慰問に訪れる。", "example_reading": "ひさいちへいも内におとずれる。", "example_meaning": "Berkunjung memberi penghiburan ke daerah terdampak bencana."},
    {"word": "慰安", "furigana": "いあん", "romaji": "ian", "meaning": "Rekreasi pelipur penat hiburan bersama", "level": "N1", "example": "社員の慰安旅行を企画する。", "example_reading": "しゃいんのいあんりょこうをきかくする。", "example_meaning": "Merencanakan liburan wisata rekreasi pelepas penat karyawan."},
    {"word": "慰労", "furigana": "いろう", "romaji": "irou", "meaning": "Apresiasi jerih payah penghargaan lelah", "level": "N1", "example": "プロジェクト完了の慰労会を開いた。", "example_reading": "ぷろじぇくとかんりょうのいろうかいをひらいた。", "example_meaning": "Mengadakan pesta apresiasi jerih payah atas tuntasnya proyek."}
])

add_kanji(4, "漏", "ロウ", "も・る、も・れる、も・らす", "Bocor merembes lolos lewat", [
    {"word": "漏洩", "furigana": "ろうえい", "romaji": "rouei", "meaning": "Kebocoran rahasia informasi data", "level": "N1", "example": "個人情報の漏洩を防ぐ対策をとる。", "example_reading": "こじんじょうほうのろうえいをふせぐたいさくをとる。", "example_meaning": "Mengambil langkah antisipasi untuk mencegah kebocoran data pribadi."},
    {"word": "漏電", "furigana": "ろうでん", "romaji": "rouden", "meaning": "Kebocoran arus arus pendek korsleting", "level": "N1", "example": "漏電により火災が発生した。", "example_reading": "ろうでんによりかさいがはっせいした。", "example_meaning": "Terjadi kebakaran yang dipicu oleh kebocoran arus listrik."},
    {"word": "遺漏", "furigana": "いろう", "romaji": "irou", "meaning": "Kelalaian kelewatan yang terlupa", "level": "N1", "example": "遺漏のないよう十分にチェックする。", "example_reading": "いろうのないようじゅうぶんにちぇっくする。", "example_meaning": "Memeriksa dengan teliti agar tidak ada hal yang terlewatkan."}
])

add_kanji(4, "盗", "トウ", "ぬす・む", "Mencuri, rampok, maling", [
    {"word": "盗難", "furigana": "とうなん", "romaji": "tounan", "meaning": "Pencurian kemalingan kehilangan", "level": "N3", "example": "自転車の盗難に遭ってしまった。", "example_reading": "じてんしゃのとうなんにあってしまった。", "example_meaning": "Sepeda saya kemalingan dicuri orang."},
    {"word": "強盗", "furigana": "ごうとう", "romaji": "goutou", "meaning": "Perampokan perampok bersenjata", "level": "N2", "example": "銀行に強盗が入った。", "example_reading": "ぎんこうにごうとうがはいった。", "example_meaning": "Perampok bersenjata masuk menyatroni bank."},
    {"word": "窃盗", "furigana": "せっとう", "romaji": "settou", "meaning": "Tindak pidana pencurian maling", "level": "N1", "example": "窃盗の容疑で逮捕された。", "example_reading": "せっとうのようぎでたいほされた。", "example_meaning": "Ditangkap polisi atas tuduhan tindak pidana pencurian."},
    {"word": "盗作", "furigana": "とうさく", "romaji": "tousaku", "meaning": "Plagiarisme penjiplakan karya", "level": "N1", "example": "他人の論文を盗作してはいけない。", "example_reading": "たにんのろんぶんをとうさくしてはいけない。", "example_meaning": "Tidak boleh menjiplak melakukan plagiarisme skripsi karya orang lain."}
])

add_kanji(4, "厳", "ゲン、ゴン", "きび・しい", "Ketat tegas keras khidmat", [
    {"word": "厳重", "furigana": "げんじゅう", "romaji": "genjuu", "meaning": "Ketat saksama penjagaan rapat", "level": "N2", "example": "貴重品を厳重に保管する。", "example_reading": "きちょうひんをげんじゅうにほかんする。", "example_meaning": "Menyimpan barang berharga dengan penjagaan yang sangat ketat."},
    {"word": "厳格", "furigana": "げんかく", "romaji": "genkaku", "meaning": "Tegas disiplin kaku tanpa kompromi", "level": "N1", "example": "厳格な家庭で育てられた。", "example_reading": "げんかくなかていでそだてられた。", "example_meaning": "Dibesarkan dalam keluarga yang berdisiplin sangat tegas."},
    {"word": "厳禁", "furigana": "げんきん", "romaji": "genkin", "meaning": "Dilarang keras mutlak dilarang", "level": "N2", "example": "館内での喫煙は厳禁です。", "example_reading": "かんないでのきつえんはげんきんです。", "example_meaning": "Merokok di dalam gedung dilarang keras."},
    {"word": "荘厳", "furigana": "そうごん", "romaji": "sougon", "meaning": "Megah agung khidmat sakral", "level": "N1", "example": "荘厳な大聖堂に圧倒された。", "example_reading": "そうごんなだいせいどうにあっとうされた。", "example_meaning": "Terkesima takjub oleh katedral yang megah nan khidmat."}
])

add_kanji(4, "遺", "イ、ユイ", "のこ・す", "Peninggalan warisan tertinggal", [
    {"word": "遺産", "furigana": "いさん", "romaji": "isan", "meaning": "Warisan harta warisan situs dunia", "level": "N2", "example": "世界文化遺産に登録された。", "example_reading": "せかいぶんかいさんにとうろくされた。", "example_meaning": "Terdaftar resmi sebagai Situs Warisan Budaya Dunia."},
    {"word": "遺跡", "furigana": "いせき", "romaji": "iseki", "meaning": "Situs peninggalan purbakala reruntuhan kuno", "level": "N2", "example": "古代エジプトの遺跡を見学する。", "example_reading": "こだいえじぷとのいせきをけんがくする。", "example_meaning": "Mengunjungi meneliti situs purbakala Mesir kuno."},
    {"word": "遺伝", "furigana": "いでん", "romaji": "iden", "meaning": "Genetika pewarisan sifat keturunan", "level": "N2", "example": "親の血液型が子供に遺伝する。", "example_reading": "おやのけつえきがたがこどもにいでんする。", "example_meaning": "Golongan darah orang tua diwariskan secara genetik ke anak."},
    {"word": "遺言", "furigana": "ゆいごん", "romaji": "yuigon", "meaning": "Surat wasiat pesan terakhir", "level": "N1", "example": "遺言に従って財産を分配した。", "example_reading": "ゆいごんにしたがってざいさんをぶんぱいした。", "example_meaning": "Membagikan harta warisan sesuai dengan isi surat wasiat."}
])

add_kanji(4, "振", "シン", "ふ・る、ふ・るう", "Goyang guncang ayun maju bangkit", [
    {"word": "振動", "furigana": "しんどう", "romaji": "shindou", "meaning": "Getaran vibrasi gerakan bolak-balik", "level": "N2", "example": "工事の音と振動が激しい。", "example_reading": "こうじのおととしんどうがはげしい。", "example_meaning": "Suara dan getaran dari proyek konstruksi sangat kencang."},
    {"word": "振興", "furigana": "しんこう", "romaji": "shinkou", "meaning": "Pemajuan revitalisasi kemajuan industri/seni", "level": "N1", "example": "地域産業の振興に力を入れる。", "example_reading": "ちいきさんぎょうのしんこうにちからをいれる。", "example_meaning": "Mencurahkan tenaga demi pemajuan industri daerah."},
    {"word": "不振", "furigana": "ふしん", "romaji": "fushin", "meaning": "Kelesuan performa buruk mandek", "level": "N1", "example": "食欲不振が続いている。", "example_reading": "しょくよくふしんがつづいている。", "example_meaning": "Nafsu makan yang menurun dan lesu terus berlanjut."}
])

add_kanji(4, "励", "レイ", "はげ・む、はげ・ます", "Semangat dorongan tekun giat", [
    {"word": "奨励", "furigana": "しょうれい", "romaji": "shourei", "meaning": "Dorongan penganjuran insentif", "level": "N1", "example": "読書を子供たちに奨励する。", "example_reading": "どくしょをごどもたちにしょうれいする。", "example_meaning": "Mendorong dan menganjurkan membaca buku kepada anak-anak."},
    {"word": "激励", "furigana": "げきれい", "romaji": "gekirei", "meaning": "Pemberian suntikan semangat mengobarkan nyali", "level": "N1", "example": "試合前に監督が選手を激励した。", "example_reading": "しあいまえにかんとくがせんしゅをげきれいした。", "example_meaning": "Pelatih menyuntikkan kobaran semangat kepada para pemain sebelum tanding."},
    {"word": "勉励", "furigana": "べんれい", "romaji": "benrei", "meaning": "Rajin tekun giat belajar/bekerja", "level": "N1", "example": "学業に勉励することを誓う。", "example_reading": "がくぎょうにべんれいすることをちかう。", "example_meaning": "Berikrar untuk tekun giat dalam menuntut ilmu pendidikan."}
])

add_kanji(4, "折", "セツ", "お・る、お・れる", "Patah lipat belok negosiasi", [
    {"word": "骨折", "furigana": "こっせつ", "romaji": "kossetsu", "meaning": "Patah tulang fraktur", "level": "N2", "example": "スキーで転倒して足を骨折した。", "example_reading": "すきーでてんとうしてあしをこっせつした。", "example_meaning": "Jatuh saat bermain ski hingga mengalami patah tulang kaki."},
    {"word": "折半", "furigana": "せっぱん", "romaji": "seppan", "meaning": "Bagi dua sama rata separuh-separuh", "level": "N1", "example": "飲食代を二人で折半した。", "example_reading": "いんしょくだいをふたりでせっぱんした。", "example_meaning": "Membagi dua sama rata biaya makan berdua."},
    {"word": "折衝", "furigana": "せっしょう", "romaji": "sesshou", "meaning": "Negosiasi alot diplomasi perundingan", "level": "N1", "example": "取引先と粘り強く価格折衝を続ける。", "example_reading": "とりひきさきとねばりづよくかかくせっしょうをつづける。", "example_meaning": "Terus melakukan negosiasi harga alot dengan klien secara gigih."},
    {"word": "屈折", "furigana": "くっせつ", "romaji": "kussetsu", "meaning": "Pembiasan refraksi cahaya", "level": "N1", "example": "水の中で光が屈折して見える。", "example_reading": "みずのなかでひかりがくっせつしてみえる。", "example_meaning": "Cahaya tampak membiaskan di dalam air."}
])

add_kanji(4, "鍵", "ケン", "かぎ", "Kunci gembok tuts tombol", [
    {"word": "鍵盤", "furigana": "けんばん", "romaji": "kemban", "meaning": "Papan tuts piano papan keyboard musik", "level": "N1", "example": "ピアノの鍵盤を軽やかに指が走る。", "example_reading": "ぴあののけんばんをかろやかにゆびがはしる。", "example_meaning": "Jari-jemari menari lincah di atas tuts piano."},
    {"word": "鍵穴", "furigana": "かぎあな", "romaji": "kagana", "meaning": "Lubang kunci pintu", "level": "N2", "example": "暗闇で鍵穴を探す。", "example_reading": "くらやみでかぎあなをさがす。", "example_meaning": "Mencari lubang kunci di tengah kegelapan."}
])

add_kanji(4, "骨", "コツ", "ほね", "Tulang kerangka struktur", [
    {"word": "骨格", "furigana": "こっかく", "romaji": "kokkaku", "meaning": "Kerangka anatomi struktur pondasi", "level": "N1", "example": "頑丈な骨格をしたアスリートだ。", "example_reading": "がんじょうなこっかくをしたあすりーとだ。", "example_meaning": "Atlet yang memiliki susunan kerangka tubuh yang sangat kokoh."},
    {"word": "接骨", "furigana": "せっこつ", "romaji": "sekkotsu", "meaning": "Penyambungan perawatan patah tulang fisioterapi", "level": "Umum", "example": "捻挫をしたので接骨院に通う。", "example_reading": "ねんざをしたのでせっこついんにかよう。", "example_meaning": "Pergi ke klinik pengobatan patah tulang/sendi karena terkilir."},
    {"word": "軟骨", "furigana": "なんこつ", "romaji": "nankotsu", "meaning": "Tulang rawan kartilago", "level": "N1", "example": "居酒屋で鶏の軟骨揚げを注文した。", "example_reading": "いざかやでとりのなんこつあげをちゅうもんした。", "example_meaning": "Memesan gorengan tulang rawan ayam di kedai izakaya."}
])

add_kanji(4, "津", "シン", "つ", "Pelabuhan muara luapan ombak", [
    {"word": "津波", "furigana": "つなみ", "romaji": "tsunami", "meaning": "Gelombang tsunami", "level": "N3", "example": "地震の後はすぐに津波警報を確認する。", "example_reading": "じしんのあとはすぐにつなみけいほうをかくにんする。", "example_meaning": "Segera pastikan peringatan tsunami setelah gempa terjadi."},
    {"word": "興味津々", "furigana": "きょうみしんしん", "romaji": "kyoumishinshin", "meaning": "Sangat penasaran meluap-luap rasa ingin tahunya", "level": "N1", "example": "新しい科学実験に興味津々だ。", "example_reading": "あたらしいかがくじっけんにきょうみしんしんだ。", "example_meaning": "Sangat penasaran meluap-luap terhadap eksperimen sains yang baru."},
    {"word": "会津", "furigana": "あいづ", "romaji": "aizu", "meaning": "Aizu (wilayah bersejarah samurai di Fukushima)", "level": "Umum", "example": "福島県の会津若松城を観光した。", "example_reading": "ふくしまけんのあいづわかまつじょうをかんこうした。", "example_meaning": "Berwisata ke Istana Aizuwakamatsu di prefektur Fukushima."}
])

add_kanji(4, "尋", "ジン", "たず・ねる", "Mencari bertanya interogasi biasa", [
    {"word": "尋問", "furigana": "じんもん", "romaji": "jimmon", "meaning": "Interogasi pemeriksaan tanya resmi", "level": "N1", "example": "裁判で証人尋問が行われた。", "example_reading": "さいばんでしょうにんじんもんがおこなわれた。", "example_meaning": "Interogasi pemeriksaan saksi dilakukan di pengadilan."},
    {"word": "尋常", "furigana": "じんじょう", "romaji": "jinjou", "meaning": "Lumrah wajar biasa (sering: 尋常ではない = luar biasa/abnormal)", "level": "N1", "example": "今年の夏の暑さは尋常ではない。", "example_reading": "ことしのなつのあつさはじんじょうではない。", "example_meaning": "Hawa panas musim panas tahun ini benar-benar tidak wajar/luar biasa."}
])

add_kanji(4, "燃", "ネン", "も・える、も・やす", "Bakar membakar api menyala", [
    {"word": "燃料", "furigana": "ねんりょう", "romaji": "nenryou", "meaning": "Bahan bakar energi", "level": "N2", "example": "車の燃料タンクを満タンにした。", "example_reading": "くるまのねんりょうたんくをまんたんにした。", "example_meaning": "Mengisi tangki bahan bakar mobil sampai penuh."},
    {"word": "燃焼", "furigana": "ねんしょう", "romaji": "nenshou", "meaning": "Pembakaran pembakaran kalori", "level": "N2", "example": "有酸素運動で脂肪を燃焼させる。", "example_reading": "ゆうさんそうんどうでしぼうをねんしょうさせる。", "example_meaning": "Membakar lemak tubuh dengan latihan aerobik."},
    {"word": "可燃", "furigana": "かねん", "romaji": "kanen", "meaning": "Mudah terbakar (sampah organik/kering)", "level": "N2", "example": "月曜日は可燃ゴミの回収日です。", "example_reading": "げつようびはかねんごみのかいしゅうびです。", "example_meaning": "Hari Senin adalah hari pengangkutan sampah yang dapat dibakar."},
    {"word": "不燃", "furigana": "ふねん", "romaji": "funen", "meaning": "Tidak mudah terbakar tahan api", "level": "N2", "example": "不燃ゴミを分別して捨てる。", "example_reading": "ふねんごみをぶんべつしてすてる。", "example_meaning": "Memilah dan membuang sampah yang tidak dapat dibakar."}
])

add_kanji(4, "蔵", "ゾウ", "くら", "Gudang penyimpanan simpan khazanah", [
    {"word": "冷蔵庫", "furigana": "れいぞうこ", "romaji": "reizouko", "meaning": "Lemari es kulkas pendingin", "level": "N4", "example": "牛乳を冷蔵庫に入れて冷やす。", "example_reading": "ぎゅうにゅうをれいぞうこにいれてひやす。", "example_meaning": "Memasukkan susu ke dalam kulkas agar dingin."},
    {"word": "貯蔵", "furigana": "ちょぞう", "romaji": "chozou", "meaning": "Penyimpanan penimbunan logistik", "level": "N2", "example": "地下の倉庫に食料を貯蔵する。", "example_reading": "ちかのそうこにしょくりょうをちょぞうする。", "example_meaning": "Menyimpan logistik bahan makanan di gudang bawah tanah."},
    {"word": "蔵書", "furigana": "ぞうしょ", "romaji": "zousho", "meaning": "Koleksi buku perpustakaan kepustakaan", "level": "N1", "example": "大学図書館は百万人分の蔵書を誇る。", "example_reading": "だいがくとしょかんはひゃくまんにんぶんのぞうしょをほこる。", "example_meaning": "Perpustakaan universitas membanggakan koleksi buku kepustakaannya yang amat banyak."},
    {"word": "埋蔵", "furigana": "まいぞう", "romaji": "maizou", "meaning": "Timbunan terpendam tersimpan di perut bumi", "level": "N1", "example": "豊富な鉱物資源が埋蔵されている。", "example_reading": "ほうふなこうぶつしげんがまいぞうされている。", "example_meaning": "Tersimpan cadangan sumber daya mineral melimpah yang terpendam di perut bumi."}
])

add_kanji(4, "創", "ソウ", "つく・る", "Menciptakan kreasi membuat luka", [
    {"word": "創造", "furigana": "そうぞう", "romaji": "souzou", "meaning": "Penciptaan kreasi ide karya baru", "level": "N2", "example": "新しい価値を創造する仕事だ。", "example_reading": "あたらしいかちをそうぞうするしごとだ。", "example_meaning": "Pekerjaan yang menciptakan nilai dan terobosan baru."},
    {"word": "創立", "furigana": "そうりつ", "romaji": "souritsu", "meaning": "Pendirian lembaga institusi sekolah", "level": "N2", "example": "母校が創立百周年を迎えた。", "example_reading": "ぼこうがそうりつひゃくしゅうねんをむかえた。", "example_meaning": "Almamater saya menyambut peringatan seabad pendirian sekolah."},
    {"word": "創作", "furigana": "そうさく", "romaji": "sousaku", "meaning": "Karya cipta kreasi sastra seni", "level": "N2", "example": "オリジナルの創作料理を考案した。", "example_reading": "おりじなるのそうさくりょうりをこうあんした。", "example_meaning": "Merancang hidangan kreasi orisinal buatan sendiri."},
    {"word": "創刊", "furigana": "そうかん", "romaji": "soukan", "meaning": "Penerbitan edisi perdana majalah koran", "level": "N1", "example": "新しいカルチャー雑誌が創刊された。", "example_reading": "あたらしいかるちゃーざっしがそうかんされた。", "example_meaning": "Majalah kebudayaan baru resmi diterbitkan untuk edisi perdana."}
])

# ==========================================
# MINGGU 5 (33 Kanji Unik)
# 暦、陰、旧、睦、如、弥、旬、諸、閏、唐、施、惑、補、慮、幼、稚、混、冒、改、善、掘、跡、墓、頂、納、就、邪、魔、測、端、竜、滝、鯉 (user wrote 補 twice)
# ==========================================
add_kanji(5, "暦", "レキ", "こよみ", "Kalender penanggalan almanak", [
    {"word": "西暦", "furigana": "せいれき", "romaji": "seireki", "meaning": "Tahun Masehi penanggalan barat", "level": "N3", "example": "日本の元号と西暦を併記する。", "example_reading": "にほんのげんごうとせいれきをへいきする。", "example_meaning": "Menuliskan tahun era Jepang berdampingan bersama tahun Masehi."},
    {"word": "還暦", "furigana": "かんれき", "romaji": "kanreki", "meaning": "Ulang tahun ke-60 (siklus zodiak kalender lengkap)", "level": "N1", "example": "父の還暦の祝いに赤いちゃんちゃんこを贈った。", "example_reading": "ちちのかんれきのいわいにあかいちゃんちゃんこをおくった。", "example_meaning": "Menghadiahi rompi merah dalam perayaan ulang tahun ayah yang ke-60."},
    {"word": "暦法", "furigana": "れきほう", "romaji": "rekihou", "meaning": "Sistem penanggalan ilmu kalender", "level": "N1", "example": "古代の天文学に基づいて暦法が作られた。", "example_reading": "こだいのてんもんがくにもとづいてれきほうがつくられた。", "example_meaning": "Sistem penanggalan dibuat berdasarkan ilmu astronomi kuno."},
    {"word": "太陽暦", "furigana": "たいようれき", "romaji": "taiyoureki", "meaning": "Kalender matahari penanggalan syamsiah", "level": "N1", "example": "現在の日本は太陽暦を採用している。", "example_reading": "げんざいのにほんはたいようれきをさいようしている。", "example_meaning": "Jepang saat ini mengadopsi kalender matahari (solar kalender)."}
])

add_kanji(5, "陰", "イン", "かげ", "Teduh bayangan suram yin", [
    {"word": "日陰", "furigana": "ひかげ", "romaji": "hikage", "meaning": "Tempat teduh naungan pohon gedung", "level": "N2", "example": "日差しが強いので日陰で休む。", "example_reading": "ひざしがつよいのでひかげでやすむ。", "example_meaning": "Beristirahat di tempat teduh karena sinar matahari sangat terik."},
    {"word": "陰気", "furigana": "いんき", "romaji": "inki", "meaning": "Muram suram kelam tidak bersemangat", "level": "N1", "example": "部屋が薄暗くて陰気な雰囲気だ。", "example_reading": "へやがうすぐらくていんきなふんいきだ。", "example_meaning": "Ruangannya temaram dan bernuansa muram suram."},
    {"word": "陰謀", "furigana": "いんぼう", "romaji": "inbou", "meaning": "Konspirasi persekongkolan jahat", "level": "N1", "example": "国家を揺るがす陰謀を阻止した。", "example_reading": "こっかをゆるがすいんぼうをそしした。", "example_meaning": "Menggagalkan konspirasi licik yang mengguncang stabilitas negara."}
])

add_kanji(5, "旧", "キュウ", "ふる・い", "Lama bekas masa lalu dahulu", [
    {"word": "旧友", "furigana": "きゅうゆう", "romaji": "kyuuyuu", "meaning": "Kawan lama sahabat masa lalu", "level": "N2", "example": "久しぶりに旧友と再会して語り合った。", "example_reading": "ひさしぶりにきゅうゆうとさいかいしてかたりあった。", "example_meaning": "Bertemu kembali dan berbincang akrab dengan kawan lama setelah sekian lama."},
    {"word": "復旧", "furigana": "ふっきゅう", "romaji": "fukkyuu", "meaning": "Pemulihan perbaikan kembali sistem/jalur rusak", "level": "N2", "example": "停電した電気が夕方に復旧した。", "example_reading": "ていでんしたでんきがゆうがたにふっきゅうした。", "example_meaning": "Listrik yang padam pulih menyala kembali pada sore hari."},
    {"word": "旧正月", "furigana": "きゅうしょうがつ", "romaji": "kyuushougatsu", "meaning": "Tahun baru Imlek penanggalan lunar", "level": "N1", "example": "アジア各地で旧正月が盛大に祝われる。", "example_reading": "あじあかくちできゅうしょうがつがせいだいにいわわれる。", "example_meaning": "Tahun baru Imlek dirayakan secara meriah di berbagai pelosok Asia."},
    {"word": "新旧", "furigana": "しんきゅう", "romaji": "shinkyuu", "meaning": "Baru dan lama masa kini dan masa lampau", "level": "N1", "example": "新旧の交代がスムーズに進む。", "example_reading": "しんきゅうのこうたいがスムーズにすすむ。", "example_meaning": "Pergantian antara yang lama dan yang baru berjalan mulus."}
])

add_kanji(5, "睦", "ボク", "むつ・まじい", "Rukun akrab harmonis bersahabat", [
    {"word": "親睦", "furigana": "しんぼく", "romaji": "shimboku", "meaning": "Mempererat tali silaturahmi keakraban rukun", "level": "N1", "example": "親睦を深めるために食事会を開く。", "example_reading": "しんぼくをふかめるためにしょくじかいをひらく。", "example_meaning": "Mengadakan jamuan makan untuk mempererat tali keakraban silaturahmi."},
    {"word": "和睦", "furigana": "わぼく", "romaji": "waboku", "meaning": "Perdamaian rekonsiliasi damai", "level": "N1", "example": "長年争っていた二国が和睦を結んだ。", "example_reading": "ながねんあらそっていたにこくがわぼくをむすんだ。", "example_meaning": "Dua negara yang berselisih bertahun-tahun akhirnya menjalin perdamaian."},
    {"word": "睦月", "furigana": "むつき", "romaji": "mutsuki", "meaning": "Mutsuki (sebutan tradisional puitis bulan Januari)", "level": "N1", "example": "睦月の寒さが身にしみる。", "example_reading": "むつきのさむさがみにしみる。", "example_meaning": "Dinginnya bulan Januari (Mutsuki) menusuk hingga ke tulang."}
])

add_kanji(5, "如", "ジョ、ニョ", "ごと・し", "Seperti bagaikan seolah-olah", [
    {"word": "突如", "furigana": "とつじょ", "romaji": "totsujo", "meaning": "Tiba-tiba sekonyong-konyong mendadak", "level": "N1", "example": "突如として大雨が降り出した。", "example_reading": "とつじょとしておおあめがふりだした。", "example_meaning": "Hujan deras tiba-tiba turun sekonyong-konyong."},
    {"word": "如実", "furigana": "にょじつ", "romaji": "nyojitsu", "meaning": "Gamblang nyata apa adanya persis kenyataan", "level": "N1", "example": "データが現状を如実に物語っている。", "example_reading": "でーたがげんじょうをにょじつにものがたっている。", "example_meaning": "Data tersebut menceritakan kondisi riil apa adanya secara gamblang."},
    {"word": "如意", "furigana": "にょい", "romaji": "nyoi", "meaning": "Sesuai kehendak hati seperti harapan", "level": "N1", "example": "万事如意に事が運ぶ。", "example_reading": "ばんじにょいにことがはこぶ。", "example_meaning": "Segala urusan berjalan mulus sesuai kehendak hati."}
])

add_kanji(5, "弥", "ミ、ビ", "いや", "Semakin mekar meluas", [
    {"word": "弥生", "furigana": "やよい", "romaji": "yayoi", "meaning": "Bulan Maret (sebutan kuno) / Zaman Yayoi bersejarah", "level": "N1", "example": "弥生時代の土器が遺跡から出土した。", "example_reading": "やよいじだいのどきがいせきからしゅつどした。", "example_meaning": "Tembikar tanah liat zaman Yayoi ditemukan dari lokasi situs purbakala."},
    {"word": "弥漫", "furigana": "びまん", "romaji": "biman", "meaning": "Menyebar merata luas kemana-mana", "level": "N1", "example": "部屋中に香水の甘い香りが弥漫している。", "example_reading": "へやじゅうにこうすいのあまいかおりがびまんしている。", "example_meaning": "Aroma wangi manis parfum menyebar semerbak merata ke seisi ruangan."},
    {"word": "弥勒", "furigana": "みろく", "romaji": "miroku", "meaning": "Bodhisattva Maitreya (Miroku Bosatsu)", "level": "Umum", "example": "京都の寺院で弥勒菩薩像を拝観する。", "example_reading": "きょうとのじいんでみろくぼさつぞうをはいかんする。", "example_meaning": "Melihat mengagumi patung Miroku Bosatsu di kuil Kyoto."}
])

add_kanji(5, "旬", "ジュン", "", "Periode 10 hari, musim hidangan paling lezat", [
    {"word": "初旬", "furigana": "しょじゅん", "romaji": "shojun", "meaning": "Awal bulan (tanggal 1 sampai 10)", "level": "N2", "example": "来月の初旬に出張が予定されている。", "example_reading": "らいげつのしょじゅんにしゅっちょうがよていされている。", "example_meaning": "Perjalanan dinas dijadwalkan pada awal bulan depan."},
    {"word": "中旬", "furigana": "ちゅうじゅん", "romaji": "chuujun", "meaning": "Pertengahan bulan (tanggal 11 sampai 20)", "level": "N2", "example": "五月中旬に桜が見頃を迎える。", "example_reading": "ごがつちゅうじゅんにさくらがみごろをむかえる。", "example_meaning": "Bunga sakura mencapai puncak mekarnya di pertengahan bulan Mei."},
    {"word": "下旬", "furigana": "げじゅん", "romaji": "gejun", "meaning": "Akhir bulan (tanggal 21 sampai akhir)", "level": "N2", "example": "月末下旬に請求書を発送する。", "example_reading": "げつまつげじゅんにせいきゅうしょをはっそうする。", "example_meaning": "Mengirimkan surat tagihan pada akhir bulan."},
    {"word": "旬", "furigana": "しゅん", "romaji": "shun", "meaning": "Musim ketika makanan sedang enak-enaknya segar", "level": "N1", "example": "秋刀魚は秋が一番の旬だ。", "example_reading": "さんまはあきがいちばんのしゅんだ。", "example_meaning": "Ikan sanma berada pada musim terenaknya saat musim gugur."}
])

add_kanji(5, "諸", "ショ", "もろ", "Aneka rupa ragam berbagai sekalian", [
    {"word": "諸君", "furigana": "しょくん", "romaji": "shokun", "meaning": "Saudara-saudara hadirin sekalian", "level": "N1", "example": "諸君の健闘を心から祈る。", "example_reading": "しょくんのけんとうをこころからいのる。", "example_meaning": "Saya mendoakan perjuangan saudara-saudara sekalian dari lubuk hati."},
    {"word": "諸島", "furigana": "しょとう", "romaji": "shotou", "meaning": "Kepulauan gugusan pulau", "level": "N2", "example": "小笠原諸島には豊かな自然がある。", "example_reading": "おがさわらしょとうにはゆたかなしぜんがある。", "example_meaning": "Kepulauan Ogasawara memiliki alam hayati yang kaya."},
    {"word": "諸悪", "furigana": "しょあく", "romaji": "shoaku", "meaning": "Segala aneka kejahatan maksiat", "level": "N1", "example": "ストレスは諸悪の根源と言われる。", "example_reading": "すとれすはしょあくのこんげんといわれる。", "example_meaning": "Stres kerap disebut sebagai akar dari segala macam penyakit keburukan."},
    {"word": "諸費用", "furigana": "しょひよう", "romaji": "shohiyou", "meaning": "Aneka rupa pengeluaran biaya administrasi", "level": "N1", "example": "契約時に諸費用が別途かかります。", "example_reading": "けいやくじにしょひようがべっとかかります。", "example_meaning": "Berbagai aneka biaya administrasi akan dikenakan terpisah saat kontrak."}
])

add_kanji(5, "閏", "ジュン", "うるう", "Kabisat interkalasi kalender", [
    {"word": "閏年", "furigana": "うるうどし", "romaji": "uruudoshi", "meaning": "Tahun kabisat (ada 29 Februari)", "level": "N2", "example": "四年に一度、二月が二十九日になる閏年が訪れる。", "example_reading": "よねんにいちど、にがつがにじゅうくにちになるうるうどしがおとずれる。", "example_meaning": "Empat tahun sekali datang tahun kabisat di mana Februari memiliki 29 hari."},
    {"word": "閏月", "furigana": "うるうづき", "romaji": "uruuzuki", "meaning": "Bulan kabisat tambahan dalam penanggalan lunar", "level": "N1", "example": "旧暦では季節のズレを調整するため閏月を設けた。", "example_reading": "きゅうれきではきせつのズレをちょうせいするためうるうづきをもうけた。", "example_meaning": "Dalam penanggalan kalender lunar disediakan bulan kabisat untuk menyesuaikan selisih musim."}
])

add_kanji(5, "唐", "トウ", "から", "Dinasti Tang Tiongkok, mendadak pedas", [
    {"word": "唐突", "furigana": "とうとつ", "romaji": "toutotsu", "meaning": "Mendadak tiba-tiba tanpa basa-basi", "level": "N1", "example": "唐突な質問に思わず返事に詰まった。", "example_reading": "とうとつなしつもんにおもわずへんじにつまった。", "example_meaning": "Saya sampai terbata-bata merespons karena pertanyaannya begitu mendadak."},
    {"word": "唐揚げ", "furigana": "からあげ", "romaji": "karaage", "meaning": "Ayam goreng tepung gurih renyah karaage", "level": "N3", "example": "居酒屋で鶏の唐揚げとビールを注文する。", "example_reading": "いざかやでとりのからあげとびーるをちゅうもんする。", "example_meaning": "Memesan ayam goreng tepung karaage dan bir di kedai izakaya."},
    {"word": "唐辛子", "furigana": "とうがらし", "romaji": "tougarashi", "meaning": "Cabai rawit bubuk cabai pedas", "level": "N2", "example": "うどんに一味唐辛子を少し振りかける。", "example_reading": "うどんにいちみとうがらしをすこしふりかける。", "example_meaning": "Menaburkan sedikit bubuk cabai merah ke atas semangkuk udon."},
    {"word": "遣唐使", "furigana": "けんとうし", "romaji": "kentoushi", "meaning": "Utusan kekaisaran Jepang ke Dinasti Tang Tiongkok", "level": "N1", "example": "遣唐使が中国から仏教や文化を持ち帰った。", "example_reading": "けんとうしがちゅうごくからぶっきょうやぶんかをもちかえった。", "example_meaning": "Utusan dinasti Tang membawa pulang ajaran Buddha dan kebudayaan dari Tiongkok."}
])

add_kanji(5, "施", "シ、セ", "ほどこ・す", "Melaksanakan terapkan subsidi amal", [
    {"word": "実施", "furigana": "じっし", "romaji": "jisshi", "meaning": "Pelaksanaan penerapan implementasi", "level": "N2", "example": "来週から新しい制度を実施する。", "example_reading": "らいしゅうからあたらしいせいどをじっしする。", "example_meaning": "Mulai minggu depan sistem baru akan diterapkan diimplementasikan."},
    {"word": "施設", "furigana": "しせつ", "romaji": "shisetsu", "meaning": "Fasilitas sarana gedung prasarana", "level": "N3", "example": "高齢者のための福祉施設を見学した。", "example_reading": "こうれいしゃのためのふくししせつをけんがくした。", "example_meaning": "Mengunjungi meninjau fasilitas kesejahteraan lansia."},
    {"word": "施行", "furigana": "しこう", "romaji": "shikou", "meaning": "Pemberlakuan berlakunya undang-undang peraturan", "level": "N1", "example": "改正法が来年四月一日に施行される。", "example_reading": "かいせいほうがおらいねんしがつついたちにしこうされる。", "example_meaning": "Undang-undang revisi akan diberlakukan mulai 1 April tahun depan."},
    {"word": "施策", "furigana": "しさく", "romaji": "shisaku", "meaning": "Kebijakan aksi langkah solutif", "level": "N1", "example": "少子化対策のための有効な施策を打ち出す。", "example_reading": "しょうしかたいさくのためのゆうこうなしさくをうちだす。", "example_meaning": "Mengeluarkan langkah kebijakan efektif untuk mengatasi penurunan angka kelahiran."}
])

add_kanji(5, "惑", "ワク", "まど・う", "Bingung ragu merepotkan planet", [
    {"word": "迷惑", "furigana": "めいわく", "romaji": "meiwaku", "meaning": "Merepotkan mengganggu gangguan", "level": "N3", "example": "近所の人に迷惑をかけないようにする。", "example_reading": "きんじょのひとにめいわくをかけないようにする。", "example_meaning": "Berusaha agar tidak merepotkan atau mengganggu warga tetangga."},
    {"word": "惑星", "furigana": "わくせい", "romaji": "wakusei", "meaning": "Planet tata surya luar angkasa", "level": "N2", "example": "太陽の周りを回る惑星を観察する。", "example_reading": "たいようのまわりをまわるわくせいをかんさつする。", "example_meaning": "Mengamati pergerakan planet-planet yang mengitari matahari."},
    {"word": "疑惑", "furigana": "ぎわく", "romaji": "giwaku", "meaning": "Kecurigaan keraguan skandal", "level": "N1", "example": "大臣の汚職疑惑が報じられた。", "example_reading": "だいじんのおしょくぎわくがほうじられた。", "example_meaning": "Kecurigaan dugaan korupsi sang menteri diberitakan media."}
])

add_kanji(5, "補", "ホ", "おぎな・う", "Menambah tambal subsidi kompensasi bantu", [
    {"word": "補助", "furigana": "ほじょ", "romaji": "hojo", "meaning": "Bantuan subsidi tunjangan bantuan", "level": "N2", "example": "市からリフォーム費用の補助金が出た。", "example_reading": "しからりふぉーむひようのほじょきんがでた。", "example_meaning": "Subsidi bantuan dana renovasi diberikan oleh pihak pemkot."},
    {"word": "補充", "furigana": "ほじゅう", "romaji": "hojuu", "meaning": "Pengisian ulang restock menambah kekurangan", "level": "N2", "example": "棚の商品を補充する作業を行う。", "example_reading": "たなのしょうひんをほじゅうするさぎょうをおこなう。", "example_meaning": "Melakukan tugas mengisi ulang barang produk di rak."},
    {"word": "補修", "furigana": "ほしゅう", "romaji": "hoshuu", "meaning": "Perbaikan tambal sulam pemeliharaan", "level": "N1", "example": "老朽化した道路を補修する工事。", "example_reading": "ろうきゅうかしたどうろをほしゅうするこうじ。", "example_meaning": "Pekerjaan konstruksi perbaikan jalan raya yang rusak dimakan usia."},
    {"word": "補償", "furigana": "ほしょう", "romaji": "hoshou", "meaning": "Kompensasi ganti kerugian klaim", "level": "N1", "example": "損害に対して正当な補償を求める。", "example_reading": "そんがいにたいしてせいとうなほしょうをもとめる。", "example_meaning": "Menuntut kompensasi ganti rugi yang setimpal atas kerugian yang dialami."}
])

add_kanji(5, "慮", "リョ", "おもんぱか・る", "Pertimbangan pemikiran cermat tenggang rasa", [
    {"word": "考慮", "furigana": "こうりょ", "romaji": "kouryo", "meaning": "Pertimbangan cermat memperhitungkan", "level": "N2", "example": "相手の立場を十分に考慮して判断する。", "example_reading": "あいてのたちばをじゅうぶんにこうりょしてはんだんする。", "example_meaning": "Membuat keputusan dengan mempertimbangkan kondisi lawan secara saksama."},
    {"word": "配慮", "furigana": "はいりょ", "romaji": "hairyo", "meaning": "Perhatian kepedulian tenggang rasa empati", "level": "N2", "example": "周囲への細やかな配慮が素晴らしい。", "example_reading": "しゅういへのこまやかなはいりょがすばらしい。", "example_meaning": "Kepedulian dan perhatiannya yang teliti terhadap lingkungan sekitar sangat mengagumkan."},
    {"word": "遠慮", "furigana": "えんりょ", "romaji": "enryo", "meaning": "Sungkan menahan diri rasa segan", "level": "N3", "example": "どうぞ遠慮せずにお召し上がりください。", "example_reading": "どうぞえんりょせずにおめしあがりください。", "example_meaning": "Silakan dimakan jangan sungkan-sungkan."},
    {"word": "熟慮", "furigana": "じゅくりょ", "romaji": "jukuryo", "meaning": "Perenungan mendalam pemikiran matang", "level": "N1", "example": "熟慮を重ねた上で結論を出した。", "example_reading": "じゅくりょをかさねたうえでけつろんをだした。", "example_meaning": "Mengeluarkan kesimpulan setelah perenungan mendalam berulang kali."}
])

add_kanji(5, "幼", "ヨウ", "おさな・い", "Kanak-kanak balita bocah kecil", [
    {"word": "幼児", "furigana": "ようじ", "romaji": "youji", "meaning": "Balita anak usia dini", "level": "N2", "example": "幼児向けの絵本を読み聞かせる。", "example_reading": "ようじむけのえほんをよみきかせる。", "example_meaning": "Membacakan buku cerita bergambar untuk anak balita."},
    {"word": "幼少", "furigana": "ようしょう", "romaji": "youshou", "meaning": "Masa kanak-kanak usia dini", "level": "N1", "example": "幼少期を海外で過ごした。", "example_reading": "ようしょうきをかいがいですごした。", "example_meaning": "Menghabiskan masa kanak-kanak di luar negeri."},
    {"word": "幼馴染", "furigana": "おさななじみ", "romaji": "osananajimi", "meaning": "Teman masa kecil sahabat sejak kecil", "level": "N2", "example": "幼馴染の結婚式に出席した。", "example_reading": "おさななじみのけっこんしきにしゅっせきした。", "example_meaning": "Menghadiri resepsi pernikahan teman masa kecil saya."}
])

add_kanji(5, "稚", "チ", "", "Kanak-kanak belia amatir belum matang", [
    {"word": "幼稚園", "furigana": "ようちえん", "romaji": "youchien", "meaning": "Taman kanak-kanak TK", "level": "N3", "example": "息子が来月から幼稚園に通う。", "example_reading": "むすこがらいげつからようちえんにかよう。", "example_meaning": "Anak laki-laki saya mulai masuk taman kanak-kanak bulan depan."},
    {"word": "稚拙", "furigana": "ちせつ", "romaji": "chisetsu", "meaning": "Kekanak-kanakan amatir kasar belum terampil", "level": "N1", "example": "文章は稚拙だが情熱が伝わってくる。", "example_reading": "ぶんしょうはちせつだがじょうねつがつたわってくる。", "example_meaning": "Meskipun tulisannya masih amatir sederhana, semangatnya terasa jelas."},
    {"word": "稚気", "furigana": "ちき", "romaji": "chiki", "meaning": "Kepolosan bocah sifat kekanak-kanakan lucu", "level": "N1", "example": "大人になっても稚気を失わない人だ。", "example_reading": "おとなになってもちきをうしなわないひとだ。", "example_meaning": "Sosok orang yang tidak kehilangan kepolosan masa kecil meski sudah dewasa."}
])

add_kanji(5, "混", "コン", "ま・ぜる、ま・じる、こ・む", "Bercampur aduk berbaur ramai padat", [
    {"word": "混乱", "furigana": "こんらん", "romaji": "konran", "meaning": "Kekacauan kebingungan huru-hara", "level": "N3", "example": "停電で駅前が大混乱に陥った。", "example_reading": "ていでんでえきまえがだいこんらんにおちいった。", "example_meaning": "Stasiun mengalami kekacauan besar akibat pemadaman listrik."},
    {"word": "混雑", "furigana": "こんざつ", "romaji": "konzatsu", "meaning": "Kepadatan keramaian berdesakan sesak", "level": "N3", "example": "朝の通勤ラッシュで電車が混雑している。", "example_reading": "あさのつうきんらっしゅででんしゃがこんざつしている。", "example_meaning": "Kereta sangat padat berdesakan pada jam sibuk berangkat kerja."},
    {"word": "混合", "furigana": "こんごう", "romaji": "kongou", "meaning": "Pencampuran percampuran komposisi senyawa", "level": "N2", "example": "複数の薬を混合して使う。", "example_reading": "ふくすうのくすりをこんごうしてつかう。", "example_meaning": "Mencampurkan beberapa jenis obat untuk digunakan."},
    {"word": "混血", "furigana": "こんけつ", "romaji": "konketsu", "meaning": "Blasteran peranakan ras campuran", "level": "N1", "example": "様々な文化背景を持つ混血の人々。", "example_reading": "さまざまなぶんかはいけいをもつこんけつのひとびと。", "example_meaning": "Orang-orang blasteran keturunan berlatar belakang berbagai budaya."}
])

add_kanji(5, "冒", "ボウ", "おか・す", "Menantang bahaya berpetualang melanggar", [
    {"word": "冒険", "furigana": "ぼうけん", "romaji": "bouken", "meaning": "Petualangan mengadu untung ekspedisi", "level": "N3", "example": "少年たちが無人島へ冒険に出かける。", "example_reading": "しょうねんたちがむじんとうへぼうけんにでかける。", "example_meaning": "Anak-anak lelaki pergi berpetualang ke pulau tak berpenghuni."},
    {"word": "冒頭", "furigana": "ぼうとう", "romaji": "boutou", "meaning": "Awal permulaan pembukaan pidato/buku", "level": "N1", "example": "スピーチの冒頭で感謝の言葉を述べた。", "example_reading": "すぴーちのぼうとうでかんしゃのことばをのべた。", "example_meaning": "Menyampaikan ungkapan terima kasih di awal pembukaan pidato."},
    {"word": "感冒", "furigana": "かんぼう", "romaji": "kambou", "meaning": "Penyakit flu batuk pilek masuk angin", "level": "N1", "example": "流行性感冒（インフルエンザ）の予防接種を受ける。", "example_reading": "りゅうこうせいかんぼうのよぼうせっしゅをうける。", "example_meaning": "Mendapatkan suntikan vaksin flu epidemi (influenza)."},
    {"word": "冒涜", "furigana": "ぼうとく", "romaji": "boutoku", "meaning": "Penodaan penistaan pelecehan kesucian", "level": "N1", "example": "神聖な場所を冒涜する行為は許されない。", "example_reading": "しんせいなばしょをぼうとくするこういはゆるされない。", "example_meaning": "Tindakan menodai menistakan tempat suci tidak dapat ditolerir."}
])

add_kanji(5, "改", "カイ", "あらた・める", "Memperbaiki merombak merevisi", [
    {"word": "改善", "furigana": "かいぜん", "romaji": "kaizen", "meaning": "Perbaikan berkelanjutan / kaizen penyempurnaan", "level": "N2", "example": "業務の効率化に向けて作業工程を改善する。", "example_reading": "ぎょうむのこうりつかにむけてさぎょうこうていをかいぜんする。", "example_meaning": "Menyempurnakan proses kerja demi efisiensi operasional."},
    {"word": "改正", "furigana": "かいせい", "romaji": "kaisei", "meaning": "Revisi amendemen pembenahan hukum undang-undang", "level": "N2", "example": "道路交通法が改正された。", "example_reading": "どうろこうつうほうがかいせいされた。", "example_meaning": "Undang-undang lalu lintas jalan raya telah direvisi."},
    {"word": "改革", "furigana": "かいかく", "romaji": "kaikaku", "meaning": "Reformasi perombakan mendasar sistem", "level": "N2", "example": "教育制度の抜本的な改革を進める。", "example_reading": "きょういくせいどのばっぽんてきなかいかくをすすめる。", "example_meaning": "Menjalankan reformasi mendasar pada sistem pendidikan."},
    {"word": "改築", "furigana": "かいちく", "romaji": "kaichiku", "meaning": "Renovasi pembangunan ulang gedung rumah", "level": "N1", "example": "古くなった実家を改築した。", "example_reading": "ふるくなったじっかをかいちくした。", "example_meaning": "Merenovasi membangun ulang rumah orang tua yang sudah tua."}
])

add_kanji(5, "善", "ゼン", "よ・い", "Baik kebajikan kebaikan optimal", [
    {"word": "改善", "furigana": "かいぜん", "romaji": "kaizen", "meaning": "Peningkatan kualitas perbaikan mutu", "level": "N2", "example": "サービスの改善に努めます。", "example_reading": "さーびすのかいぜんにつとめます。", "example_meaning": "Kami berusaha keras dalam meningkatkan mutu pelayanan."},
    {"word": "善悪", "furigana": "ぜんあく", "romaji": "zen'aku", "meaning": "Baik dan buruk benar dan salah", "level": "N2", "example": "子供に善悪の区別を教える。", "example_reading": "こどもにぜんあくのくべつをおしえる。", "example_meaning": "Mengajarkan perbedaan mana yang baik dan mana yang buruk pada anak."},
    {"word": "親善", "furigana": "しんぜん", "romaji": "shinzen", "meaning": "Persahabatan bilateral muhibah diplomasi", "level": "N1", "example": "両国の親善試合が行われた。", "example_reading": "りょうこくのしんぜんじあかがおこなわれた。", "example_meaning": "Pertandingan persahabatan antar kedua negara digelar."},
    {"word": "善処", "furigana": "ぜんしょ", "romaji": "zensho", "meaning": "Penanganan terbaik langkah bijak optimal", "level": "N1", "example": "ご要望にお応えできるよう善処いたします。", "example_reading": "ごようぼうにおこたえできるようぜんしょいたします。", "example_meaning": "Kami akan menangani dengan sebaik mungkin demi memenuhi permohonan Anda."}
])

add_kanji(5, "掘", "クツ", "ほ・る", "Menggali menambang mengorek", [
    {"word": "発掘", "furigana": "はっくつ", "romaji": "hakkutsu", "meaning": "Penggalian arkeologi ekskavasi / penemuan bakat", "level": "N1", "example": "遺跡から古代の土器が発掘された。", "example_reading": "いせきからこだいのどきがはっくつされた。", "example_meaning": "Tembikar kuno digali ditemukan dari situs purbakala."},
    {"word": "採掘", "furigana": "さいくつ", "romaji": "saikutsu", "meaning": "Penambangan penggalian bijih tambang", "level": "N1", "example": "海底の油田から石油を採掘する。", "example_reading": "かいていのゆでんからせきゆをさいくつする。", "example_meaning": "Menambang minyak bumi dari ladang minyak bawah laut."},
    {"word": "掘削", "furigana": "くっさく", "romaji": "kussaku", "meaning": "Pengeboran penggalian terowongan", "level": "N1", "example": "トンネルを掘削する大型機械を導入する。", "example_reading": "とんねるをくっさくするおおがたきかいをどうにゅうする。", "example_meaning": "Mendatangkan mesin raksasa untuk mengebor menggali terowongan."}
])

add_kanji(5, "跡", "セキ", "あと", "Jejak bekas situs tapak", [
    {"word": "遺跡", "furigana": "いせき", "romaji": "iseki", "meaning": "Situs bersejarah reruntuhan purbakala", "level": "N2", "example": "世界遺産に指定された遺跡を巡る旅。", "example_reading": "せかいいさんにしていされたいせきをめぐるたび。", "example_meaning": "Perjalanan keliling mengunjungi situs purbakala warisan dunia."},
    {"word": "足跡", "furigana": "あしあと", "romaji": "ashiato", "meaning": "Jejak tapak kaki langkah", "level": "N2", "example": "雪の上に動物の足跡が残っている。", "example_reading": "ゆきのうえにどうぶつのあしあとがのこっている。", "example_meaning": "Jejak kaki hewan tertinggal di atas salju tebal."},
    {"word": "追跡", "furigana": "ついせき", "romaji": "tsuiseki", "meaning": "Pelacakan pengejaran tracking paket", "level": "N1", "example": "荷物の配送状況をネットで追跡する。", "example_reading": "にもつのはいそうじょうきょうをねっとでついせきする。", "example_meaning": "Melacak status pengiriman paket logistik lewat internet."},
    {"word": "奇跡", "furigana": "きせき", "romaji": "kiseki", "meaning": "Keajaiban mukjizat luar biasa", "level": "N2", "example": "奇跡的に全員が無事救出された。", "example_reading": "きせきてきにぜんいんがぶじきゅうしゅつされた。", "example_meaning": "Secara mukjizat ajaib semua orang berhasil diselamatkan tanpa luka."}
])

add_kanji(5, "墓", "ボ", "はか", "Makam kuburan nisan", [
    {"word": "墓地", "furigana": "ぼち", "romaji": "bochi", "meaning": "Kompleks pemakaman kuburan umum", "level": "N2", "example": "小高い丘の上にある静かな墓地。", "example_reading": "こだかいおかのうえにあるしずかなぼち。", "example_meaning": "Area pemakaman tenang yang terletak di atas bukit kecil."},
    {"word": "墓参り", "furigana": "はかまいり", "romaji": "hakamairi", "meaning": "Ziarah kubur nyekar makam leluhur", "level": "N2", "example": "お盆に家族そろって墓参りに行く。", "example_reading": "おぼんにかぞくそろってはかまいりにいく。", "example_meaning": "Pergi ziarah kubur bersama sekeluarga saat hari raya Obon."},
    {"word": "墓石", "furigana": "ぼせき", "romaji": "boseki", "meaning": "Batu nisan makam", "level": "N1", "example": "墓石をきれいに水で洗って清める。", "example_reading": "ぼせきをきれいにみずであらってきよめる。", "example_meaning": "Mencuci bersih batu nisan dengan air untuk menyucikannya."}
])

add_kanji(5, "頂", "チョウ", "いただ・く、いただき", "Puncak apex menerima dengan hormat", [
    {"word": "頂上", "furigana": "ちょうじょう", "romaji": "choujou", "meaning": "Puncak gunung puncak tebing", "level": "N2", "example": "険しい山道を登りきって頂上に着いた。", "example_reading": "けわしいやまみちをのぼりきってちょうじょうについた。", "example_meaning": "Tiba di puncak setelah mendaki jalan setapak gunung yang curam."},
    {"word": "頂点", "furigana": "ちょうてん", "romaji": "chouten", "meaning": "Titik puncak apex kulminasi prestasi", "level": "N1", "example": "世界の頂点に立つ夢を叶えた。", "example_reading": "せかいのちょうてんにたつゆめをかなえた。", "example_meaning": "Mewujudkan impian untuk berdiri di puncak dunia."},
    {"word": "山頂", "furigana": "さんちょう", "romaji": "sanchou", "meaning": "Puncak bukit / puncak pegunungan", "level": "N2", "example": "山頂からの景色は息をのむほど美しい。", "example_reading": "さんちょうからのけしきはいきをのむほどうつくしい。", "example_meaning": "Pemandangan dari puncak gunung sangat menakjubkan memesona."},
    {"word": "登頂", "furigana": "とうちょう", "romaji": "touchou", "meaning": "Berhasil mendaki mencapai puncak", "level": "N1", "example": "エベレストの登頂に成功した。", "example_reading": "えべれすとのとうちょうにせいこうした。", "example_meaning": "Berhasil mendaki menaklukkan puncak gunung Everest."}
])

add_kanji(5, "納", "ノウ、ナッ", "おさ・める、おさ・まる", "Bayar pasok serah simpan puas", [
    {"word": "納得", "furigana": "なっとく", "romaji": "nattoku", "meaning": "Paham menerima berpuas sepakat masuk akal", "level": "N3", "example": "説明を聞いて納得した。", "example_reading": "せつめいをきいてなっとくした。", "example_meaning": "Saya paham dan menerima setelah mendengar penjelasannya."},
    {"word": "納税", "furigana": "のうぜい", "romaji": "nouzei", "meaning": "Pembayaran pajak pelunasan pajak", "level": "N2", "example": "国民には納税の義務がある。", "example_reading": "こくみんにはのうぜいのぎむがある。", "example_meaning": "Warga negara memiliki kewajiban membayar pajak."},
    {"word": "納品", "furigana": "のうひん", "romaji": "nouhin", "meaning": "Pengiriman barang pesanan pasokan delivery", "level": "N2", "example": "注文された商品を期日通りに納品する。", "example_reading": "ちゅうもんされたしょうひんをきじつどおりにのうひんする。", "example_meaning": "Mengirimkan pasokan barang yang dipesan tepat sesuai tenggat waktu."},
    {"word": "収納", "furigana": "しゅうのう", "romaji": "shuunou", "meaning": "Penyimpanan penataan barang lemari", "level": "N2", "example": "この部屋は収納スペースがたくさんある。", "example_reading": "このへやはしゅうのうすぺーすがたくさんある。", "example_meaning": "Kamar ini memiliki banyak ruang tempat penyimpanan barang."}
])

add_kanji(5, "就", "シュウ、ジュ", "つ・く、つ・ける", "Menjabat mulai kerja tidur masuk posisi", [
    {"word": "就職", "furigana": "しゅうしょく", "romaji": "shuushoku", "meaning": "Mendapatkan pekerjaan masuk dunia kerja", "level": "N3", "example": "大学を卒業して商社に就職した。", "example_reading": "だいがくをそつぎょうしてしょうしゃにしゅうしょくした。", "example_meaning": "Lulus kuliah lalu mendapatkan pekerjaan di perusahaan dagang."},
    {"word": "就任", "furigana": "しゅうにん", "romaji": "shuunin", "meaning": "Pelantikan pengangkatan memangku jabatan", "level": "N2", "example": "新しい代表取締役に就任する。", "example_reading": "あたらしいだいひょうとりしまりやくにしゅうにんする。", "example_meaning": "Dilantik resmi memangku jabatan sebagai direktur utama yang baru."},
    {"word": "就寝", "furigana": "しゅうしん", "romaji": "shuushin", "meaning": "Pergi tidur waktu istirahat tidur", "level": "N2", "example": "毎日十一時には就寝するようにしている。", "example_reading": "まいにちじゅういちじにはしゅうしんするようにしている。", "example_meaning": "Saya membiasakan diri untuk pergi tidur pada jam 11 malam setiap hari."},
    {"word": "就労", "furigana": "しゅうろう", "romaji": "shuurou", "meaning": "Bekerja pelaksanaan izin kerja", "level": "N1", "example": "日本での就労ビザを取得した。", "example_reading": "にほんでのしゅうろうびざをしゅとくした。", "example_meaning": "Mendapatkan visa izin kerja di Jepang."}
])

add_kanji(5, "邪", "ジャ", "", "Jahat dengki rintangan pilek", [
    {"word": "邪魔", "furigana": "じゃま", "romaji": "jama", "meaning": "Gangguan menghalangi mengacau", "level": "N3", "example": "勉強の邪魔をしないでください。", "example_reading": "べんきょうのじゃまをしないでください。", "example_meaning": "Tolong jangan mengganggu waktu belajar saya."},
    {"word": "風邪", "furigana": "かぜ", "romaji": "kaze", "meaning": "Masuk angin flu batuk pilek", "level": "N4", "example": "風邪をひいて熱が出た。", "example_reading": "かぜをひいてねつがでた。", "example_meaning": "Masuk angin flu dan badan demam."},
    {"word": "邪念", "furigana": "じゃねん", "romaji": "janen", "meaning": "Pikiran jahat godaan nafsu kotor", "level": "N1", "example": "邪念を捨てて瞑想に集中する。", "example_reading": "じゃねんをすててめいそうにしゅうちゅうする。", "example_meaning": "Membuang segala pikiran kotor dan fokus pada meditasi."},
    {"word": "無邪気", "furigana": "むじゃき", "romaji": "mujaki", "meaning": "Polos tanpa prasangka lugu bersih hati", "level": "N2", "example": "子供が無邪気に笑っている。", "example_reading": "こどもがむじゃきにわらっている。", "example_meaning": "Anak kecil tertawa dengan begitu polos dan lepas."}
])

add_kanji(5, "魔", "マ", "", "Sihir iblis setan misteri", [
    {"word": "魔法", "furigana": "まほう", "romaji": "mahou", "meaning": "Sihir keajaiban sulap", "level": "N3", "example": "魔法使いが呪文を唱えた。", "example_reading": "まほうつかいがじゅもんをとなえた。", "example_meaning": "Penyihir merapalkan mantra sihir."},
    {"word": "悪魔", "furigana": "あくま", "romaji": "akuma", "meaning": "Iblis setan iblis laknat", "level": "N2", "example": "悪魔のような残忍な犯行だ。", "example_reading": "あくまのようなざんにんなはんこうだ。", "example_meaning": "Tindak kejahatan yang keji bengis bagai iblis."},
    {"word": "魔力", "furigana": "まりょく", "romaji": "maryoku", "meaning": "Kekuatan magis daya tarik gaib memikat", "level": "N1", "example": "人を惹きつけてやまない不思議な魔力がある。", "example_reading": "ひとをひきつけてやまないふしぎなまりょくがある。", "example_meaning": "Memiliki kekuatan magis misterius yang terus memikat hati orang."}
])

add_kanji(5, "測", "ソク", "はか・る", "Mengukur mengestimasi menduga", [
    {"word": "測定", "furigana": "そくてい", "romaji": "sokutei", "meaning": "Pengukuran dimensi berat kadar", "level": "N2", "example": "健康診断で血圧を測定する。", "example_reading": "けんこうしんだんでけつあつをそくていする。", "example_meaning": "Mengukur tekanan darah dalam tes pemeriksaan kesehatan."},
    {"word": "予測", "furigana": "よそく", "romaji": "yosoku", "meaning": "Prediksi prakiraan ramalan tren", "level": "N2", "example": "今後の市場動向を予測する。", "example_reading": "こんごのしじょうどうこうをよそくする。", "example_meaning": "Memprediksi tren pergerakan pasar ke depan."},
    {"word": "推測", "furigana": "すいそく", "romaji": "suisoku", "meaning": "Dugaan tebakan estimasi penalaran", "level": "N2", "example": "状況から犯人の動機を推測する。", "example_reading": "じょうきょうからはんにんのどうきをすいそくする。", "example_meaning": "Menduga motif pelaku dari rangkaian situasi di lokasi."},
    {"word": "測量", "furigana": "そくりょう", "romaji": "sokuryou", "meaning": "Survei pemetaan tanah topografi", "level": "N1", "example": "道路建設のために土地を測量する。", "example_reading": "どうろけんせつのためにとちをそくりょうする。", "example_meaning": "Melakukan survei pengukuran tanah untuk pembangunan jalan raya."}
])

add_kanji(5, "端", "タン", "はし、は、はた", "Ujung tepi pangkal ekstrem", [
    {"word": "極端", "furigana": "きょくたん", "romaji": "kyokutan", "meaning": "Ekstrem berlebihan ujung ke ujung", "level": "N2", "example": "極端な例を出して説明する。", "example_reading": "きょくたんなれいをだしてせつめいする。", "example_meaning": "Menjelaskan dengan memberikan contoh kasus yang ekstrem."},
    {"word": "先端", "furigana": "せんたん", "romaji": "sentan", "meaning": "Ujung terdepan tercanggih frontier", "level": "N1", "example": "先端技術を駆使して新製品を開発した。", "example_reading": "せんたんぎじゅつをくししてしんせいひんをかいはつした。", "example_meaning": "Mengembangkan produk baru dengan memanfaatkan teknologi mutakhir terdepan."},
    {"word": "端緒", "furigana": "たんしょ", "romaji": "tansho", "meaning": "Titik awal mula petunjuk permulaan jalan keluar", "level": "N1", "example": "問題解決への端緒をつかむ。", "example_reading": "もんだいかいけつへのたんしょをつかむ。", "example_meaning": "Menangkap titik awal petunjuk menuju solusi pemecahan masalah."},
    {"word": "中途半端", "furigana": "ちゅうとはんぱ", "romaji": "chuutohampa", "meaning": "Setengah-setengah tanggung tidak tuntas", "level": "N2", "example": "仕事を中途半端なまま放置してはいけない。", "example_reading": "しごとをちゅうとはんぱなままほうちしてはいけない。", "example_meaning": "Tidak boleh membiarkan pekerjaan terbengkalai setengah-setengah."}
])

add_kanji(5, "竜", "リュウ、リョウ", "たつ", "Naga raksasa", [
    {"word": "恐竜", "furigana": "きょうりゅう", "romaji": "kyouryuu", "meaning": "Dinosaurus kadal raksasa purba", "level": "N2", "example": "博物館に恐竜の巨大な化石が展示されている。", "example_reading": "はくぶつかんにきょうりゅうのきょだいなかせきがてんじされている。", "example_meaning": "Fosil dinosaurus raksasa dipamerkan di museum."},
    {"word": "竜巻", "furigana": "たつまき", "romaji": "tatsumaki", "meaning": "Angin puting beliung tornado", "level": "N2", "example": "竜巻が発生して家屋に被害が出た。", "example_reading": "たつまきがはっせいしてかおくにごがいがでた。", "example_meaning": "Angin puting beliung melanda dan menimbulkan kerusakan pada rumah-rumah."},
    {"word": "竜頭蛇尾", "furigana": "りゅうとうだび", "romaji": "ryuutoudabi", "meaning": "Awalnya hebat menggebu akhirnya melempem", "level": "N1", "example": "壮大な計画だったが竜頭蛇尾に終わってしまった。", "example_reading": "そうだいなけいかくだったりゅうとうだびにおわってしまった。", "example_meaning": "Rencana yang awalnya megah namun akhirnya berakhir antiklimaks mengecewakan."}
])

add_kanji(5, "滝", "ロウ", "たき", "Air terjun jeram riam", [
    {"word": "滝壺", "furigana": "たきつぼ", "romaji": "takitsubo", "meaning": "Kolam dasar air terjun cekungan air", "level": "N1", "example": "激しい水が滝壺に吸い込まれていく。", "example_reading": "はげしいみずがたきつぼにすいこまれていく。", "example_meaning": "Curahan air yang deras terhisap masuk ke dalam kolam dasar air terjun."},
    {"word": "白滝", "furigana": "しらたき", "romaji": "shirataki", "meaning": "Mi shirataki konyaku kenyal / riam putih", "level": "Umum", "example": "すき焼きに白滝を入れると美味しい。", "example_reading": "すきやきにしらたきをいれるとおいしい。", "example_meaning": "Sangat lezat jika menambahkan mi shirataki ke dalam masakan sukiyaki."},
    {"word": "瀑布", "furigana": "ばくふ", "romaji": "bakufu", "meaning": "Air terjun besar riam megah curahan tinggi", "level": "N1", "example": "那智の瀑布を遠くから望む。", "example_reading": "なちのばくふをとおくからのぞむ。", "example_meaning": "Memandang air terjun raksasa Nachi dari kejauhan."}
])

add_kanji(5, "鯉", "リ", "こい", "Ikan karper koi", [
    {"word": "錦鯉", "furigana": "にしきごい", "romaji": "nishikigoi", "meaning": "Ikan koi hias corak warna-warni Jepang", "level": "Umum", "example": "庭の池で美しい錦鯉が優雅に泳いでいる。", "example_reading": "にわのいけでうつくしいにしきごいがゆうがにおよいでいる。", "example_meaning": "Ikan koi hias berenang anggun di kolam taman."},
    {"word": "鯉のぼり", "furigana": "こいのぼり", "romaji": "koinobori", "meaning": "Koinobori (bendera umbul-umbul ikan koi hari anak)", "level": "N2", "example": "五月の空に鯉のぼりが元気にたなびく。", "example_reading": "ごがつのそらにこいのぼりがげんきにたなびく。", "example_meaning": "Bendera koinobori berkibar riang di angkasa bulan Mei."}
])

# ==========================================
# MINGGU 6 (17 Kanji)
# 鉛 (user: 铅), 削, 瓶, 排, 鋭 (user: 锐), 属, 錆 (user: 锈), 捜 (user: 搜), 跳, 遺 (user: 遗), 嫁, 躍 (user: 跃), 維 (user: 维), 税, 咳, 潮, 癖
# ==========================================
add_kanji(6, "鉛", "エン", "なまり", "Timbal timah hitam timah pensil", [
    {"word": "鉛筆", "furigana": "えんぴつ", "romaji": "empitsu", "meaning": "Pensil kayu tulis", "level": "N4", "example": "鉛筆を削ってノートに文字を書く。", "example_reading": "えんぴつをけずってのーとにもじをかく。", "example_meaning": "Meraut pensil lalu menulis huruf di buku catatan."},
    {"word": "亜鉛", "furigana": "あえん", "romaji": "aen", "meaning": "Seng zinc mineral logam", "level": "N1", "example": "健康のために亜鉛のサプリメントを飲む。", "example_reading": "けんこうのためにあえんのさぷりめんとをのむ。", "example_meaning": "Meminum suplemen zinc (seng) demi menjaga kesehatan."},
    {"word": "鉛筆削り", "furigana": "えんぴつけずり", "romaji": "empitsukezuri", "meaning": "Rautan penyerut pensil", "level": "Umum", "example": "机の上に鉛筆削りを置く。", "example_reading": "つくえのうえにえんぴつけずりをおく。", "example_meaning": "Meletakkan rautan serutan pensil di atas meja kerja."}
], note="Input varian: 铅")

add_kanji(6, "削", "サク", "けず・る", "Meraut memotong mengurangi kikis", [
    {"word": "削減", "furigana": "さくげん", "romaji": "sakugen", "meaning": "Pengurangan pemotongan anggaran emisi", "level": "N2", "example": "経費を大幅に削減することに成功した。", "example_reading": "けいひをおおはばにさくげんすることにせいこうした。", "example_meaning": "Berhasil memotong mengurangi pengeluaran operasional secara drastis."},
    {"word": "添削", "furigana": "てんさく", "romaji": "tensaku", "meaning": "Koreksi penyuntingan memeriksa tulisan tugas", "level": "N1", "example": "先生に小論文を添削してもらった。", "example_reading": "せんせいにしょうろんぶんをてんさくしてもらった。", "example_meaning": "Mendapat koreksi penyuntingan esai ilmiah dari guru."},
    {"word": "削除", "furigana": "さくじょ", "romaji": "sakujo", "meaning": "Penghapusan penghapusan data delete", "level": "N2", "example": "不要なファイルをフォルダーから削除した。", "example_reading": "ふようなふぁいるをふぉるだーからさくじょした。", "example_meaning": "Menghapus berkas yang tidak terpakai dari folder."}
])

add_kanji(6, "瓶", "ビン", "かめ", "Botol toples guci vas", [
    {"word": "花瓶", "furigana": "かびん", "romaji": "kabin", "meaning": "Vas bunga tempat bunga", "level": "N3", "example": "テーブルの上の花瓶にバラを生けた。", "example_reading": "てーぶるのうえのかびんにばらをいけた。", "example_meaning": "Menata bunga mawar di vas bunga di atas meja."},
    {"word": "空き瓶", "furigana": "あきびん", "romaji": "akibin", "meaning": "Botol kaca kosong", "level": "N2", "example": "ジュースの空き瓶をリサイクルに出す。", "example_reading": "じゅーすのあきびんをりさいくるにだす。", "example_meaning": "Mengeluarkan botol kaca kosong bekas jus untuk didaur ulang."},
    {"word": "瓶詰", "furigana": "びんづめ", "romaji": "bindzume", "meaning": "Makanan kemasan botol kaca selai asinan", "level": "N1", "example": "手作りのジャムを瓶詰にして保存する。", "example_reading": "てづくりのじゃむをびんづめにしてほぞんする。", "example_meaning": "Mengemas selai buatan sendiri ke dalam botol kaca untuk disimpan."},
    {"word": "魔法瓶", "furigana": "まほうびん", "romaji": "mahoubin", "meaning": "Termos botol penahan panas dingin", "level": "N2", "example": "魔法瓶に温かいお茶を入れて持参する。", "example_reading": "まほうびんにあたたかいおちゃをいれてじさんする。", "example_meaning": "Membawa teh hangat di dalam termos air."}
])

add_kanji(6, "排", "ハイ", "", "Mengeluarkan mengusir menolak limbah", [
    {"word": "排除", "furigana": "はいじょ", "romaji": "haijo", "meaning": "Penyingkiran eksklusi mengeliminasi rintangan", "level": "N1", "example": "あらゆる不正を徹底的に排除する。", "example_reading": "あらゆるふせいをてっていてきにはいじょする。", "example_meaning": "Menyingkirkan mengeliminasi segala kecurangan hingga tuntas."},
    {"word": "排出", "furigana": "はいしゅつ", "romaji": "haishutsu", "meaning": "Pengeluaran pembuangan emisi limbah gas", "level": "N1", "example": "温室効果ガスの排出量をゼロにする。", "example_reading": "おんしつこうかがすのはいしゅつりょうをぜろにする。", "example_meaning": "Menurunkan volume pembuangan emisi gas rumah kaca hingga nol."},
    {"word": "排気", "furigana": "はいき", "romaji": "haiki", "meaning": "Gas buang pembuangan udara knalpot", "level": "N2", "example": "車の排気ガスが空気を汚染する。", "example_reading": "くるまのはいきがすがくうきをおせんする。", "example_meaning": "Gas buang knalpot mobil mencemari udara."},
    {"word": "排他", "furigana": "はいた", "romaji": "haita", "meaning": "Eksklusif penolakan terhadap pihak luar", "level": "N1", "example": "排他的な態度は国際社会で孤立を招く。", "example_reading": "はいたてきなたいどはこくさいしゃかいでこりつをまねく。", "example_meaning": "Sikap eksklusif menutup diri mengundang isolasi di masyarakat internasional."}
])

add_kanji(6, "鋭", "エイ", "するど・い", "Tajam runcing peka tanggap", [
    {"word": "鋭敏", "furigana": "えいびん", "romaji": "eibin", "meaning": "Peka tajam indra tanggap cepat", "level": "N1", "example": "犬は非常に鋭敏な嗅覚を持っている。", "example_reading": "いぬはひじょうにえいびんなきゅうかくをもっている。", "example_meaning": "Anjing memiliki indra penciuman yang sangat tajam peka."},
    {"word": "鋭気", "furigana": "えいき", "romaji": "eiki", "meaning": "Semangat membara energi tekad yang kuat", "level": "N1", "example": "休日に温泉に入って鋭気を養う。", "example_reading": "きゅうじつにおんせんにはいってえいきをやしなう。", "example_meaning": "Memulihkan memupuk semangat membara dengan berendam di air panas saat libur."},
    {"word": "精鋭", "furigana": "せいえい", "romaji": "seiei", "meaning": "Pasukan elit prajurit terbaik pilihan", "level": "N1", "example": "社内から選りすぐりの精鋭部隊を集めた。", "example_reading": "しゃないからえりすぐりのせいえいぶたいをあつめた。", "example_meaning": "Mengumpulkan tim elit terpilih dari seantero internal perusahaan."},
    {"word": "鋭角", "furigana": "えいかく", "romaji": "eikaku", "meaning": "Sudut lancip (kurang dari 90 derajat)", "level": "N1", "example": "直角三角形の一つの角は鋭角だ。", "example_reading": "ちょっかくさんかくけいのひとつの角はえいかくだ。", "example_meaning": "Salah satu sudut segitiga siku-siku adalah sudut lancip."}
], note="Input varian: 锐")

add_kanji(6, "属", "ゾク", "", "Tergolong anggota berafiliasi subordinat", [
    {"word": "所属", "furigana": "しょぞく", "romaji": "shozoku", "meaning": "Berafiliasi menjadi anggota dari regu/instansi", "level": "N2", "example": "大学の合唱サークルに所属している。", "example_reading": "だいがくのがっしょうさーくるにしょぞくしている。", "example_meaning": "Tergabung berafiliasi dalam klub paduan suara universitas."},
    {"word": "金属", "furigana": "きんぞく", "romaji": "kinzoku", "meaning": "Logam metal besi", "level": "N3", "example": "空港の保安検査で金属探知機を通る。", "example_reading": "くうこうのほあんけんさできんぞくたんちきをとおる。", "example_meaning": "Melewati alat pendeteksi logam di pemeriksaan keamanan bandara."},
    {"word": "付属", "furigana": "ふぞく", "romaji": "fuzoku", "meaning": "Terlampir aksesori pelengkap afiliasi sekolah", "level": "N2", "example": "説明書に付属のCD-ROMが付いている。", "example_reading": "せつめいしょにふぞくのしーでぃーろむがついている。", "example_meaning": "CD-ROM pelengkap terlampir bersama buku petunjuk panduan."},
    {"word": "専属", "furigana": "せんぞく", "romaji": "senzoku", "meaning": "Kontrak eksklusif khusus satu pihak", "level": "N1", "example": "有名ブランドの専属モデルとして活躍する。", "example_reading": "ゆうめいぶらんどのせんぞくもでるとしてかつやくする。", "example_meaning": "Berkiprah sebagai model kontrak eksklusif merek ternama."}
])

add_kanji(6, "錆", "ショウ", "さび、さび・る", "Karat berkarat noda logam", [
    {"word": "防錆", "furigana": "ぼうせい", "romaji": "bousei", "meaning": "Antikarat perlindungan pencegah karat", "level": "N1", "example": "金属の部品に防錆スプレーを吹き付ける。", "example_reading": "きんぞくのぶひんにぼうせいすぷれーをふきつける。", "example_meaning": "Menyemprotkan semprotan antikarat pada komponen logam."},
    {"word": "錆止め", "furigana": "さびどめ", "romaji": "sabidome", "meaning": "Cat pelapis penahan karat", "level": "Umum", "example": "鉄のフェンスに錆止め塗料を塗る。", "example_reading": "てつのふぇんすにさびどめとりょうをぬる。", "example_meaning": "Mengoleskan cat penahan karat pada pagar besi."},
    {"word": "赤錆", "furigana": "あかさび", "romaji": "akasabi", "meaning": "Karat merah pada logam besi", "level": "N1", "example": "古い水道管に赤錆が発生していた。", "example_reading": "ふるいすいどうかんにあかさびがはっせいしていた。", "example_meaning": "Karat merah terbentuk timbul pada pipa saluran air tua."}
], note="Input varian: 锈")

add_kanji(6, "捜", "ソウ", "さが・す", "Mencari menggeledah investigasi", [
    {"word": "捜索", "furigana": "そうさく", "romaji": "sousaku", "meaning": "Pencarian orang hilang/barang SAR", "level": "N1", "example": "警察と消防が山で行方不明者を捜索した。", "example_reading": "けいさつとしょうぼうがやまでゆくえふめいしゃをそうさくした。", "example_meaning": "Polisi dan pemadam kebakaran mencari korban hilang di gunung."},
    {"word": "捜査", "furigana": "そうさ", "romaji": "sousa", "meaning": "Investigasi penyelidikan kepolisian", "level": "N2", "example": "事件の真相を解明するために捜査本部が設置された。", "example_reading": "じけんのしんそうをかいめいするためにそうさほんぶがせっちされた。", "example_meaning": "Markas investigasi didirikan untuk mengungkap fakta kasus perkara."},
    {"word": "家宅捜索", "furigana": "かたくそうさく", "romaji": "katakusousaku", "meaning": "Penggeledahan rumah oleh penegak hukum", "level": "N1", "example": "容疑者の自宅に家宅捜索が入った。", "example_reading": "ようぎしゃのじたくにかたくそうさくがはいった。", "example_meaning": "Penggeledahan rumah dilakukan di kediaman tersangka."}
], note="Input varian: 搜")

add_kanji(6, "跳", "チョウ", "と・ぶ、は・ねる", "Melompat meloncat memantul", [
    {"word": "跳躍", "furigana": "ちょうやく", "romaji": "chouyaku", "meaning": "Lompatan loncatan terbang tinggi", "level": "N1", "example": "バレエダンサーが見事な跳躍を見せた。", "example_reading": "ばれえだんさーがみごとなちょうやくをみせた。", "example_meaning": "Penari balet memperlihatkan lompatan loncatan yang amat memukau."},
    {"word": "高跳び", "furigana": "たかとび", "romaji": "takatobi", "meaning": "Lompat tinggi cabang atletik", "level": "N2", "example": "陸上競技の走り高跳びで新記録を出した。", "example_reading": "りくじょうきょうぎのはしりたかとびでしんきろくをだした。", "example_meaning": "Mencetak rekor baru dalam cabang atletik lompat tinggi."},
    {"word": "幅跳び", "furigana": "はばとび", "romaji": "habatobi", "meaning": "Lompat jauh cabang atletik", "level": "N2", "example": "走り幅跳びの練習に励む。", "example_reading": "はしりはばとびのれんしゅうにはげむ。", "example_meaning": "Tekun giat berlatih cabang lompat jauh."}
])

add_kanji(6, "遺", "イ、ユイ", "のこ・す", "Peninggalan warisan tertinggal", [
    {"word": "遺族", "furigana": "いぞく", "romaji": "izoku", "meaning": "Keluarga yang ditinggalkan ahli waris keluarga duka", "level": "N1", "example": "事故の遺族に深い哀悼の意を捧げる。", "example_reading": "じこのいぞくにふかいあいとうのいをささげる。", "example_meaning": "Menyampaikan belasungkawa duka mendalam kepada keluarga korban yang ditinggalkan."},
    {"word": "遺失物", "furigana": "いしつぶつ", "romaji": "ishitsubutsu", "meaning": "Barang hilang tercecer lost and found", "level": "N1", "example": "電車の遺失物取扱所で傘を受け取った。", "example_reading": "でんしゃのいしつぶつとりあつかいじょでかさをうけとった。", "example_meaning": "Mengambil payung di loket barang hilang lost and found kereta api."},
    {"word": "遺志", "furigana": "いし", "romaji": "ishi", "meaning": "Kehendak cita-cita mulia mendiang almarhum", "level": "N1", "example": "亡き恩師の遺志を継いで研究を続ける。", "example_reading": "なきおんしのいしをついでけんきゅうをつづける。", "example_meaning": "Melanjutkan penelitian demi meneruskan cita-cita mulia mendiang sang guru."},
    {"word": "遺産", "furigana": "いさん", "romaji": "isan", "meaning": "Harta peninggalan warisan luhur", "level": "N2", "example": "祖父から受け継いだ大切な遺産だ。", "example_reading": "そふからうけついだたいせつないさんだ。", "example_meaning": "Harta warisan penting yang diwarisi dari sang kakek."}
], note="Input varian: 遗 (Muncul di Minggu 4 dan Minggu 6)")

add_kanji(6, "嫁", "カ", "よめ、とつ・ぐ", "Mempelai wanita pengantin melempar beban", [
    {"word": "転嫁", "furigana": "てんか", "romaji": "tenka", "meaning": "Melempar tanggung jawab kesalahan pada orang lain", "level": "N1", "example": "自分の失敗を他人に責任転嫁してはいけない。", "example_reading": "じぶんのしっぱいをたにんにせきにんてんかしてはいけない。", "example_meaning": "Tidak boleh melempar tanggung jawab kesalahan diri sendiri kepada orang lain."},
    {"word": "嫁入り", "furigana": "よめいり", "romaji": "yomeiri", "meaning": "Pernikahan pengantin mempelai wanita bersanding", "level": "N1", "example": "娘の嫁入りの道具をそろえる。", "example_reading": "むすめのよめいりのどうぐをそろえる。", "example_meaning": "Mempersiapkan perlengkapan perbekalan pengantin putri tercinta."},
    {"word": "嫁姑", "furigana": "よめしゅうとめ", "romaji": "yomeshutome", "meaning": "Hubungan menantu wanita dan ibu mertua", "level": "Umum", "example": "嫁姑の関係を円満に保つ工夫。", "example_reading": "よめしゅうとめのかんけいをえんまんにたもつくふう。", "example_meaning": "Kiat menjaga keharmonisan rukun hubungan menantu dan mertua."}
])

add_kanji(6, "躍", "ヤク", "おど・る", "Melompat melonjak dinamis", [
    {"word": "活躍", "furigana": "かつやく", "romaji": "katsuyaku", "meaning": "Kiprah gemilang kesuksesan berprestasi aktif", "level": "N3", "example": "海外のリーグで日本人選手が大活躍している。", "example_reading": "かいがいのりーぐでにほんじんせんしゅがだいかつやくしている。", "example_meaning": "Pemain asal Jepang berkiprah sangat sukses di liga luar negeri."},
    {"word": "飛躍", "furigana": "ひやく", "romaji": "hiyaku", "meaning": "Lompatan kemajuan drastis pesat", "level": "N1", "example": "技術の飛躍的な進歩により生活が一変した。", "example_reading": "ぎじゅつのひやくてきなしんぽによりせいかつがいっぺんした。", "example_meaning": "Kehidupan berubah total berkat lompatan kemajuan teknologi yang sangat pesat."},
    {"word": "躍動", "furigana": "やくどう", "romaji": "yakudou", "meaning": "Dinamisme lincah penuh energi gerak hidup", "level": "N1", "example": "若者の躍動感あふれるダンスパフォーマンス。", "example_reading": "わかもののやくどうかんあふれるだんすぱふぉーまんす。", "example_meaning": "Pertunjukan tarian anak muda yang meluap penuh dinamisme lincah berenergi."},
    {"word": "躍進", "furigana": "やくしん", "romaji": "yakushin", "meaning": "Langkah terobosan maju meroket", "level": "N1", "example": "新興企業が市場で目覚ましい躍進を遂げた。", "example_reading": "しんこうきぎょうがしじょうでめざましいやくしんをとげた。", "example_meaning": "Perusahaan rintisan menorehkan langkah terobosan pesat di pasar."}
], note="Input varian: 跃")

add_kanji(6, "維", "イ", "", "Mengikat memelihara serat benang", [
    {"word": "維持", "furigana": "いじ", "romaji": "iji", "meaning": "Pemeliharaan mempertahankan kestabilan kondisi", "level": "N2", "example": "健康な体型を維持するために毎日ジョギングする。", "example_reading": "けんこうなたいけいをいじするためにまいにちじょぎんぐする。", "example_meaning": "Jogging setiap hari demi memelihara bentuk tubuh yang sehat."},
    {"word": "繊維", "furigana": "せんい", "romaji": "sen'i", "meaning": "Serat tekstil / serat makanan pangan fiber", "level": "N2", "example": "食物繊維が豊富な野菜を積極的に食べる。", "example_reading": "しょくもつせんいがほうふなやさいをせっきょくてきにたべる。", "example_meaning": "Rajin mengonsumsi sayur-mayur yang kaya akan serat pangan."},
    {"word": "明治維新", "furigana": "めいじいしん", "romaji": "meijiishin", "meaning": "Restorasi Meiji (reformasi zaman modern Jepang)", "level": "N1", "example": "明治維新によって日本の近代化が急速に進んだ。", "example_reading": "めいじいしんによってにほんのきんだいかがきゅうそくにすすんだ。", "example_meaning": "Modernisasi Jepang bergerak maju sangat pesat berkat Restorasi Meiji."}
], note="Input varian: 维")

add_kanji(6, "税", "ゼイ", "", "Pajak retribusi bea", [
    {"word": "税金", "furigana": "ぜいきん", "romaji": "zeikin", "meaning": "Uang pajak pembayaran pajak", "level": "N3", "example": "所得に応じた税金を納める。", "example_reading": "しょとくにおうじたぜいきんをおさめる。", "example_meaning": "Membayar uang pajak sesuai dengan jumlah penghasilan."},
    {"word": "消費税", "furigana": "しょうひぜい", "romaji": "shouhizei", "meaning": "Pajak pertambahan nilai (PPN) / konsumsi", "level": "N2", "example": "買い物をする時に十パーセントの消費税がかかる。", "example_reading": "かいものをするじゅうぱーせんとのしょうひぜいがかかる。", "example_meaning": "Dikenakan pajak konsumsi sebesar 10% saat berbelanja."},
    {"word": "免税", "furigana": "めんぜい", "romaji": "menzei", "meaning": "Bebas pajak tax-free duty-free", "level": "N2", "example": "空港の免税店で香水とチョコレートを買った。", "example_reading": "くうこうのめんぜいてんでこうすいとちょこれーとをかった。", "example_meaning": "Membeli parfum dan cokelat di toko bebas pajak bandara."},
    {"word": "増税", "furigana": "ぞうぜい", "romaji": "zouzei", "meaning": "Kenaikan tarif pajak penambahan pajak", "level": "N1", "example": "来年度からの増税案が国会で審議される。", "example_reading": "らいねんどからのぞうぜいあんがこっかいでしんぎされる。", "example_meaning": "Rancangan kenaikan tarif pajak mulai tahun depan dibahas di parlemen."}
])

add_kanji(6, "咳", "ガイ", "せき", "Batuk batuk-batuk", [
    {"word": "咳払い", "furigana": "せきばらい", "romaji": "sekibarai", "meaning": "Berdehem membersihkan tenggorokan memberi aba-aba", "level": "N1", "example": "軽く咳払いをしてから話し始めた。", "example_reading": "かるくせきばらいをしてからはなしはじめた。", "example_meaning": "Berdehem pelan terlebih dahulu sebelum mulai berbicara."},
    {"word": "乾咳", "furigana": "からぜき", "romaji": "karazeki", "meaning": "Batuk kering tanpa dahak", "level": "N1", "example": "乾燥した部屋で乾咳が止まらなくなった。", "example_reading": "かんそうしたへやだからぜきがとまらなくなった。", "example_meaning": "Batuk kering tidak kunjung reda di dalam ruangan yang kering."},
    {"word": "鎮咳", "furigana": "ちんがい", "romaji": "chingai", "meaning": "Pereda batuk obat batuk antitusif", "level": "N1", "example": "喉の痛みを抑える鎮咳薬を服用する。", "example_reading": "のどのいたみをおさえるちんがいやくをふくようする。", "example_meaning": "Meminum obat pereda batuk untuk meredakan sakit tenggorokan."}
])

add_kanji(6, "潮", "チョウ", "しお", "Pasang surut air laut arus zaman", [
    {"word": "風潮", "furigana": "ふうちょう", "romaji": "fuuchou", "meaning": "Arus tren sosial zaman kecenderungan masyarakat", "level": "N1", "example": "最近の若者の間で広がる新しい風潮だ。", "example_reading": "さいきんのわかもののあいだでひろがるあたらしいふうちょうだ。", "example_meaning": "Ini adalah arus tren baru yang meluas di kalangan generasi muda saat ini."},
    {"word": "満潮", "furigana": "まんちょう", "romaji": "manchou", "meaning": "Pasang air laut pasang puncak", "level": "N2", "example": "満潮の時間を調べてから海釣りに出かける。", "example_reading": "まんちょうのじかんをしらべてからうみづりにでかける。", "example_meaning": "Memeriksa waktu pasang laut sebelum pergi memancing ke laut."},
    {"word": "干潮", "furigana": "かんちょう", "romaji": "kanchou", "meaning": "Surut air laut pasang surut terendah", "level": "N2", "example": "干潮時に現れる砂浜を散歩する。", "example_reading": "かんちょうじにあらわれるすなはまをさんぽする。", "example_meaning": "Berjalan santai di pantai berpasir yang muncul saat air surut."},
    {"word": "潮時", "furigana": "しおどき", "romaji": "shiodoki", "meaning": "Momentum pas saat yang tepat untuk pensiun/mundur", "level": "N1", "example": "ここが引き際の潮時だと判断した。", "example_reading": "ここがひきぎわのしおどきだとはんだんした。", "example_meaning": "Memutuskan bahwa inilah saat momentum yang tepat untuk mundur."}
])

add_kanji(6, "癖", "ヘキ", "くせ", "Kebiasaan tingkah tabiat khas", [
    {"word": "悪癖", "furigana": "あくへき", "romaji": "akuheki", "meaning": "Kebiasaan buruk tabiat jelek", "level": "N1", "example": "爪を噛む悪癖を直したい。", "example_reading": "つめをかむあくへきをなおしたい。", "example_meaning": "Saya ingin menghilangkan kebiasaan buruk menggigit kuku."},
    {"word": "潔癖", "furigana": "けっぺき", "romaji": "keppeki", "meaning": "Sangat cinta kebersihan / pantang kotor perfeksionis", "level": "N1", "example": "彼女は潔癖症で一日中掃除をしている。", "example_reading": "かのじょはけっぺきしょうでいちにちじゅうそうじをしている。", "example_meaning": "Dia memiliki sifat sangat cinta kebersihan dan menyapu sepanjang hari."},
    {"word": "口癖", "furigana": "くちぐせ", "romaji": "kuchiguse", "meaning": "Kata ucapan yang sering terlontar kebiasaan berucap", "level": "N2", "example": "「大丈夫」が彼の口癖になっている。", "example_reading": "だいじょうぶがかれのくちぐせになっている。", "example_meaning": "Kata 'tidak apa-apa' sudah menjadi ucapan khas kebiasaannya."},
    {"word": "手癖", "furigana": "てぐせ", "romaji": "teguse", "meaning": "Kebiasaan tangan usil / kebiasaan memainkan jari", "level": "N1", "example": "ペンを回すのが彼の手癖だ。", "example_reading": "ぺんをまわすのがかれのてぐせだ。", "example_meaning": "Memutar-mutar pena adalah kebiasaan tangan usilnya."}
])

print(f"Total kanji compiled: {len(DATA)}")
weeks = {}
total_jukugo = 0
for k in DATA:
    w = k["week"]
    weeks[w] = weeks.get(w, 0) + 1
    total_jukugo += len(k["jukugo"])

print(f"Weeks summary: {weeks}")
print(f"Total Jukugo: {total_jukugo}")

# Export to data.js
js_content = f"// Dataset Jukugo Master\n// Diperbarui otomatis dengan data lengkap Minggu 1 - 6\n\nconst JUKUGO_DATABASE = {json.dumps(DATA, ensure_ascii=False, indent=2)};\n\nif (typeof module !== 'undefined' && module.exports) {{\n  module.exports = JUKUGO_DATABASE;\n}}\n"

with open("C:/Users/Pujo Lestariono/.gemini/antigravity/scratch/jukugo-master/data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("data.js successfully written!")
