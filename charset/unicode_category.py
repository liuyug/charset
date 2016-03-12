#!/usr/bin/env python
# encoding: utf-8

panel0 = (
((0x0000, 0x001F), u'C0控制符', u'C0_Controls'),
((0x0020, 0x007F), u'基本拉丁文', u'Basic_Latin'),
((0x0080, 0x009F), u'C1控制符', u'C1_Controls',),
((0x00A0, 0x00FF), u'拉丁文补充-1', u'Latin-1_Supplement',),
((0x0100, 0x017F), u'拉丁文扩展-A', u'Latin_Extended-A',),
((0x0180, 0x024F), u'拉丁文扩展-B', u'Latin_Extended-B',),
((0x0250, 0x02AF), u'国际音标扩展', u'IPA_Extensions',),
((0x02B0, 0x02FF), u'占位修饰符号', u'Spacing_Modifier_Letters',),
((0x0300, 0x036F), u'结合附加符号', u'Combining_Diacritics_Marks',),
((0x0370, 0x03FF), u'希腊字母及科普特字母', u'Greek_and_Coptic',),
((0x0400, 0x04FF), u'西里尔字母', u'Cyrillic',),
((0x0500, 0x052F), u'西里尔字母补充', u'Cyrillic_Supplement',),
((0x0530, 0x058F), u'亚美尼亚字母', u'Armenian',),
((0x0590, 0x05FF), u'希伯来文', u'Hebrew',),
((0x0600, 0x06FF), u'阿拉伯文', u'Arabic',),
((0x0700, 0x074F), u'叙利亚文', u'Syriac',),
((0x0750, 0x077F), u'阿拉伯文补充', u'Arabic_Supplement',),
((0x0780, 0x07BF), u'它拿字母', u'Thaana',),
((0x07C0, 0x07FF), u'西非書面文字', u'N_Ko',),
((0x0800, 0x083F), u'撒玛利亚字母', u'Samaritan',),
((0x0840, 0x085F), u'曼达文字', u'Mandaic',),
((0x0860, 0x08FF), u'阿拉伯文扩展-A', u'Arabic_Extended-A',),
((0x0900, 0x097F), u'天城文', u'Devanagari',),
((0x0980, 0x09FF), u'孟加拉文', u'Bengali',),
((0x0A00, 0x0A7F), u'古木基文', u'Gurmukhi',),
((0x0A80, 0x0AFF), u'古吉拉特文', u'Gujarati',),
((0x0B00, 0x0B7F), u'奥里亚文', u'Oriya',),
((0x0B80, 0x0BFF), u'泰米尔文', u'Tamil',),
((0x0C00, 0x0C7F), u'泰卢固文', u'Telugu',),
((0x0C80, 0x0CFF), u'卡纳达文', u'Kannada',),
((0x0D00, 0x0D7F), u'马拉雅拉姆文', u'Malayalam',),
((0x0D80, 0x0DFF), u'僧伽罗文', u'Sinhala',),
((0x0E00, 0x0E7F), u'泰文', u'Thai',),
((0x0E80, 0x0EFF), u'老挝文', u'Lao',),
((0x0F00, 0x0FFF), u'藏文', u'Tibetan',),
((0x1000, 0x109F), u'缅甸文', u'Myanmar',),
((0x10A0, 0x10FF), u'格鲁吉亚字母', u'Georgian',),
((0x1100, 0x11FF), u'諺文字母', u'Hangul_Jamo',),
((0x1200, 0x137F), u'吉兹字母', u'Ethiopic',),
((0x1380, 0x139F), u'吉兹字母补充', u'Ethiopic_Supplement',),
((0x13A0, 0x13FF), u'切罗基字母', u'Cherokee',),
((0x1400, 0x167F), u'统一加拿大原住民音節文字', u'Unified_Canadian_Aboriginal_Syllabics',),
((0x1680, 0x169F), u'欧甘字母', u'Ogham',),
((0x16A0, 0x16FF), u'卢恩字母', u'Runic',),
((0x1700, 0x171F), u'他加禄字母', u'Tagalog',),
((0x1720, 0x173F), u'哈努诺文', u'Hanunóo',),
((0x1740, 0x175F), u'布希德文', u'Buhid',),
((0x1760, 0x177F), u'塔格巴努亚文', u'Tagbanwa',),
((0x1780, 0x17FF), u'高棉文', u'Khmer',),
((0x1800, 0x18AF), u'蒙古文', u'Mongolian',),
((0x18B0, 0x18FF), u'加拿大原住民音節文字扩展', u'Unified_Canadian_Aboriginal_Syllabics_Extended',),
((0x1900, 0x194F), u'林布文', u'Limbu',),
((0x1950, 0x197F), u'德宏傣文', u'Tai_Le',),
((0x1980, 0x19DF), u'新傣仂文', u'New_Tai_Lue',),
((0x19E0, 0x19FF), u'高棉文符号', u'Khmer_Symbols',),
((0x1A00, 0x1A1F), u'布吉文', u'Buginese',),
((0x1A20, 0x1AAF), u'老傣文', u'Tai_Tham',),
((0x1AB0, 0x1AFF), u'组合变音标记扩展', u'Combining_Diacritical_Marks_Extended',),
((0x1B00, 0x1B7F), u'巴厘字母', u'Balinese',),
((0x1B80, 0x1BBF), u'巽他字母', u'Sundanese',),
((0x1BC0, 0x1BFF), u'巴塔克文', u'Batak',),
((0x1C00, 0x1C4F), u'雷布查字母', u'Lepcha',),
((0x1C50, 0x1C7F), u'桑塔利文', u'Ol_Chiki',),
((0x1C80, 0x1CBF), u'待定', u'undefined',),
((0x1CC0, 0x1CCF), u'巽他字母补充', u'Sudanese_Supplement',),
((0x1CD0, 0x1CFF), u'梵文吠陀扩展', u'Vedic_Extensions',),
((0x1D00, 0x1D7F), u'音标扩展', u'Phonetic_Extensions',),
((0x1D80, 0x1DBF), u'音标扩展补充', u'Phonetic_Extensions_Supplement',),
((0x1DC0, 0x1DFF), u'结合附加符号补充', u'Combining_Diacritics_Marks_Supplement',),
((0x1E00, 0x1EFF), u'拉丁文扩展附加', u'Latin_Extended_Additional',),
((0x1F00, 0x1FFF), u'希腊语扩展', u'Greek_Extended',),
((0x2000, 0x206F), u'常用标点', u'General_Punctuation',),
((0x2070, 0x209F), u'上标及下标', u'Superscripts_and_Subscripts',),
((0x20A0, 0x20CF), u'货币符号', u'Currency_Symbols',),
((0x20D0, 0x20FF), u'组合用记号', u'Combining_Diacritics_Marks_for_Symbols',),
((0x2100, 0x214F), u'字母式符号', u'Letterlike_Symbols',),
((0x2150, 0x218F), u'数字形式', u'Number_Forms',),
((0x2190, 0x21FF), u'箭头', u'Arrows',),
((0x2200, 0x22FF), u'数学运算符', u'Mathematical_Operators',),
((0x2300, 0x23FF), u'杂项工业符号', u'Miscellaneous_Technical',),
((0x2400, 0x243F), u'控制图片', u'Control_Pictures',),
((0x2440, 0x245F), u'光学识别符', u'Optical_Character_Recognition',),
((0x2460, 0x24FF), u'带圈字母和数字', u'Enclosed_Alphanumerics',),
((0x2500, 0x257F), u'制表符', u'Box_Drawing',),
((0x2580, 0x259F), u'方块元素', u'Block_Elements',),
((0x25A0, 0x25FF), u'几何图形', u'Geometric_Shapes',),
((0x2600, 0x26FF), u'杂项符号', u'Miscellaneous_Symbols',),
((0x2700, 0x27BF), u'装饰符号', u'Dingbats',),
((0x27C0, 0x27EF), u'杂项数学符号-A', u'Miscellaneous_Mathematical_Symbols-A',),
((0x27F0, 0x27FF), u'追加箭头-A', u'Supplemental_Arrows-A',),
((0x2800, 0x28FF), u'盲文点字模型', u'Braille_Patterns',),
((0x2900, 0x297F), u'追加箭头-B', u'Supplemental_Arrows-B',),
((0x2980, 0x29FF), u'杂项数学符号-B', u'Miscellaneous_Mathematical_Symbols-B',),
((0x2A00, 0x2AFF), u'追加数学运算符', u'Supplemental_Mathematical_Operator',),
((0x2B00, 0x2BFF), u'杂项符号和箭头', u'Miscellaneous_Symbols_and_Arrows',),
((0x2C00, 0x2C5F), u'格拉哥里字母', u'Glagolitic',),
((0x2C60, 0x2C7F), u'拉丁文扩展-C', u'Latin_Extended-C',),
((0x2C80, 0x2CFF), u'科普特字母', u'Coptic',),
((0x2D00, 0x2D2F), u'格鲁吉亚字母补充', u'Georgian_Supplement',),
((0x2D30, 0x2D7F), u'提非纳文', u'Tifinagh',),
((0x2D80, 0x2DDF), u'吉兹字母扩展', u'Ethiopic_Extended',),
((0x2DE0, 0x2DFF), u'西里尔字母扩展-A', u'Cyrillic_Extended-A',),
((0x2E00, 0x2E7F), u'追加标点', u'Supplemental_Punctuation',),
((0x2E80, 0x2EFF), u'中日韩汉字部首补充', u'CJK_Radicals_Supplement',),
((0x2F00, 0x2FDF), u'康熙部首', u'Kangxi_Radicals',),
((0x2FF0, 0x2FFF), u'表意文字序列', u'Ideographic_Description_Characters',),
((0x3000, 0x303F), u'中日韩符号和标点', u'CJK_Symbols_and_Punctuation',),
((0x3040, 0x309F), u'日文平假名', u'Hiragana',),
((0x30A0, 0x30FF), u'日文片假名', u'Katakana',),
((0x3100, 0x312F), u'注音字母', u'Bopomofo',),
((0x3130, 0x318F), u'谚文兼容字母', u'Hangul_Compatibility_Jamo',),
((0x3190, 0x319F), u'汉文注释标志', u'Kanbun',),
((0x31A0, 0x31BF), u'注音字母扩展', u'Bopomofo_Extended',),
((0x31C0, 0x31EF), u'中日韩笔画', u'CJK_Strokes',),
((0x31F0, 0x31FF), u'日文片假名拼音扩展', u'Katakana_Phonetic_Extensions',),
((0x3200, 0x32FF), u'带圈的CJK字符及月份', u'Enclosed_CJK_Letters_and_Months',),
((0x3300, 0x33FF), u'中日韩兼容字符', u'CJK_Compatibility',),
((0x3400, 0x4DBF), u'中日韩统一表意文字扩展A', u'CJK_Unified_Ideographs_Extension_A',),
((0x4DC0, 0x4DFF), u'易经六十四卦符号', u'Yijing_Hexagrams_Symbols',),
((0x4E00, 0x9FFF), u'中日韩统一表意文字', u'CJK_Unified_Ideographs',),
((0xA000, 0xA48F), u'彝文音节', u'Yi_Syllables',),
((0xA490, 0xA4CF), u'彝文字根', u'Yi_Radicals',),
((0xA4D0, 0xA4FF), u'老傈僳文', u'Lisu',),
((0xA500, 0xA63F), u'瓦伊语', u'Vai',),
((0xA640, 0xA69F), u'西里尔字母扩展-B', u'Cyrillic_Extended-B',),
((0xA6A0, 0xA6FF), u'巴姆穆文字', u'Bamum',),
((0xA700, 0xA71F), u'修饰用声调符号', u'Modifier_Tone_Letters',),
((0xA720, 0xA7FF), u'拉丁文扩展-D', u'Latin_Extended-D',),
((0xA800, 0xA82F), u'锡尔赫特文', u'Syloti_Nagri',),
((0xA830, 0xA83F), u'通用印度数字格式', u'Common_Indic_Number_Forms',),
((0xA840, 0xA87F), u'八思巴文字', u'Phags-pa',),
((0xA880, 0xA8DF), u'索拉什特拉文', u'Saurashtra',),
((0xA8E0, 0xA8FF), u'天城文扩展', u'Devanagari_Extended',),
((0xA900, 0xA92F), u'克耶里字母', u'Kayah_Li',),
((0xA930, 0xA95F), u'勒姜字母', u'Rejang',),
((0xA960, 0xA97F), u'谚文扩展-A', u'Hangul_Jamo_Extended-A',),
((0xA980, 0xA9DF), u'爪哇字母', u'Javanese',),
((0xA9E0, 0xA9FF), u'缅甸文扩展-B', u'Myanmar_Extended-B',),
((0xAA00, 0xAA5F), u'占语字母', u'Cham',),
((0xAA60, 0xAA7F), u'缅甸文扩展-A', u'Myanmar_Extended-A',),
((0xAA80, 0xAADF), u'越南傣文', u'Tai_Viet',),
((0xAAE0, 0xAAFF), u'曼尼普尔文扩展', u'Meetei_Mayek_Extensions',),
((0xAB00, 0xAB2F), u'吉兹字母扩展-A', u'Ethiopic_Extended-A',),
((0xAB30, 0xAB6F), u'拉丁文扩展-E', u'Latin_Extended-E',),
((0xAB70, 0xABBF), u'切罗基语补充', u'Cherokee_Supplement',),
((0xABC0, 0xABFF), u'曼尼普尔文', u'Meetei_Mayek',),
((0xAC00, 0xD7AF), u'谚文音节', u'Hangul_Syllables',),
((0xD7B0, 0xD7FF), u'谚文字母扩展-B', u'Hangul_Jamo_Extended-B',),
((0xD800, 0xDBFF), u'UTF-16的高半区', u'High-half_zone_of_UTF-16',),
((0xDC00, 0xDFFF), u'UTF-16的低半区', u'Low-half_zone_of_UTF-16',),
((0xE000, 0xF8FF), u'私用区', u'Private_Use_Area',),
((0xF900, 0xFAFF), u'中日韩兼容表意文字', u'CJK_Compatibility_Ideographs',),
((0xFB00, 0xFB4F), u'字母表達形式（拉丁字母连字、亚美尼亚字母连字、希伯来文表现形式）', u'Alphabetic_Presentation_Forms',),
((0xFB50, 0xFDFF), u'阿拉伯字母表達形式-A', u'Arabic_Presentation_Forms_A',),
((0xFE00, 0xFE0F), u'異體字选择符', u'Variation_Selector',),
((0xFE10, 0xFE1F), u'竖排形式', u'Vertical_Forms',),
((0xFE20, 0xFE2F), u'组合用半符号', u'Combining_Half_Marks',),
((0xFE30, 0xFE4F), u'中日韩兼容形式', u'CJK_Compatibility_Forms',),
((0xFE50, 0xFE6F), u'小寫变体形式', u'Small_Form_Variants',),
((0xFE70, 0xFEFF), u'阿拉伯文表達形式-B', u'Arabic_Presentation_Forms_B',),
((0xFF00, 0xFFEF), u'半形及全形字符', u'Halfwidth_and_Fullwidth_Forms',),
((0xFFF0, 0xFFFF), u'特殊', u'Specials',),
)

panel1 = (
((0x10000, 0x1007F), u'线形文字B音节文字', u'Linear_B_Syllabary'),
((0x10080, 0x100FF), u'线形文字B表意文字', u'Linear_B_Ideograms'),
((0x10100, 0x1013F), u'爱琴海数字', u'Aegean_Numbers'),
((0x10140, 0x1018F), u'古希腊数字', u'Ancient_Greek_Numbers'),
((0x10190, 0x101CF), u'古代记数系统', u'Ancient_Symbols'),
((0x101D0, 0x101FF), u'费斯托斯圆盘', u'Phaistos_Disc'),
((0x10280, 0x1029F), u'吕基亚字母', u'Lycian'),
((0x102A0, 0x102DF), u'卡利亚字母', u'Carian'),
((0x102E0, 0x102FF), u'科普特闰余数字', u'Coptic_Epact_Numbers'),
((0x10300, 0x1032F), u'古意大利字母', u'Old_Italic'),
((0x10330, 0x1034F), u'哥特字母', u'Gothic'),
((0x10350, 0x1037F), u'古彼尔姆文', u'Old_Permic'),
((0x10380, 0x1039F), u'乌加里特字母', u'Ugaritic'),
((0x103A0, 0x103DF), u'古波斯楔形文字', u'Old_Persian'),
((0x10400, 0x1044F), u'德赛莱特字母', u'Deseret'),
((0x10450, 0x1047F), u'萧伯纳字母', u'Shavian'),
((0x10480, 0x104AF), u'奥斯曼亚字母', u'Osmanya'),
((0x10500, 0x1052F), u'艾尔巴桑字母', u'Elbasan'),
((0x10530, 0x1056F), u'高加索阿尔巴尼亚文', u'Caucasian_Albanian'),
((0x10600, 0x1077F), u'线形文字A', u'Linear_A'),
((0x10800, 0x1083F), u'塞浦路斯音节文字', u'Cypriot_Syllabary'),
((0x10840, 0x1085F), u'帝国亚兰文字', u'Imperial_Aramaic'),
((0x10860, 0x1087F), u'帕尔迈拉字母', u'Palmyrene'),
((0x10880, 0x108AF), u'纳巴泰字母', u'Nabataean'),
((0x108E0, 0x108FF), u'哈坦文', u'Hatran'),
((0x10900, 0x1091F), u'腓尼基字母', u'Phoenician'),
((0x10920, 0x1093F), u'吕底亚字母', u'Lydian'),
((0x10980, 0x1099F), u'麦罗埃文圣书体', u'Meroitic_Hieroglyphs'),
((0x109A0, 0x109FF), u'麦罗埃文草书体', u'Meroitic_Cursive'),
((0x10A00, 0x10A5F), u'佉卢文', u'Kharoshthi'),
((0x10A60, 0x10A7F), u'古南阿拉伯字母', u'Old_South_Arabian'),
((0x10A80, 0x10A9F), u'古北阿拉伯字母', u'Old_North_Arabian'),
((0x10AC0, 0x10AFF), u'摩尼字母', u'Manichaean'),
((0x10B00, 0x10B3F), u'阿维斯陀字母', u'Avestan'),
((0x10B40, 0x10B5F), u'碑刻帕提亚文', u'Inscriptional_Parthian'),
((0x10B60, 0x10B7F), u'碑刻巴列维文', u'Inscriptional_Pahlavi'),
((0x10B80, 0x10BAF), u'诗篇巴列维文', u'Psalter_Pahlavi'),
((0x10C00, 0x10C4F), u'古突厥文', u'Old_Turkic'),
((0x10C80, 0x10CFF), u'古匈牙利字母', u'Old_Hungarian'),
((0x10E60, 0x10E7F), u'卢米文数字', u'Rumi_Numeral_Symbols'),
((0x11000, 0x1107F), u'婆罗米文字', u'Brahmi'),
((0x11080, 0x110CF), u'凯提文', u'Kaithi'),
((0x110D0, 0x110FF), u'索拉桑朋文', u'Sora_Sompeng'),
((0x11100, 0x1114F), u'查克马文', u'Chakma'),
((0x11150, 0x1117F), u'马哈佳尼文', u'Mahajani'),
((0x11180, 0x111DF), u'夏拉达文', u'Sharada'),
((0x111E0, 0x111FF), u'古僧伽罗文数字', u'Sinhala_Archaic_Numbers'),
((0x11200, 0x1124F), u'可吉文', u'Khojki'),
((0x11280, 0x112AF), u'穆尔塔妮文', u'Multani'),
((0x112B0, 0x112FF), u'库达瓦迪文', u'Khudawadi'),
((0x11300, 0x1137F), u'帕拉瓦文', u'Grantha'),
((0x11480, 0x114DF), u'提尔胡塔文', u'Tirhuta'),
((0x11580, 0x115FF), u'悉昙文字', u'Siddham'),
((0x11600, 0x1165F), u'莫迪文', u'Modi'),
((0x11680, 0x116CF), u'塔克里字母', u'Takri'),
((0x11700, 0x1173F), u'阿豪姆文字', u'Ahom'),
((0x118A0, 0x118FF), u'瓦兰齐地文', u'Warang_Citi'),
((0x11AC0, 0x11AFF), u'袍清豪文', u'Pau_Cin_Hau'),
((0x12000, 0x123FF), u'楔形文字', u'Cuneiform'),
((0x12400, 0x1247F), u'楔形文字数字和标点符号', u'Cuneiform_Numbers_and_Punctuation'),
((0x12480, 0x1254F), u'早期王朝楔形文字', u'Early_Dynastic_Cuneiform'),
((0x13000, 0x1342F), u'埃及圣书体', u'Egyptian_Hieroglyphs'),
((0x14400, 0x1467F), u'安納托利亞象形文字', u'Anatolian_Hieroglyphs'),
((0x16800, 0x16A3F), u'巴姆穆文字补充', u'Bamum_Supplement'),
((0x16A40, 0x16A6F), u'默文', u'Mro'),
((0x16AD0, 0x16AFF), u'巴萨哇文字', u'Bassa_Vah'),
((0x16B00, 0x16B8F), u'帕哈苗文', u'Pahawh_Hmong'),
((0x16F00, 0x16F9F), u'柏格理苗文', u'Miao'),
((0x1B000, 0x1B0FF), u'日文假名补充', u'Kana_Supplement'),
((0x1BC00, 0x1BC9F), u'杜普雷速记', u'Duployan'),
((0x1BCA0, 0x1BCAF), u'速记格式控制符', u'Shorthand_Format_Controls'),
((0x1D000, 0x1D0FF), u'拜占庭音乐符号', u'Byzantine_Musical_Symbols'),
((0x1D100, 0x1D1FF), u'音乐符号', u'Musical_Symbols'),
((0x1D200, 0x1D24F), u'古希腊音乐记号', u'Ancient_Greek_Musical_Notation'),
((0x1D300, 0x1D35F), u'太玄经符号', u'Tai_Xuan_Jing_Symbols'),
((0x1D360, 0x1D37F), u'算筹', u'Counting_Rod_Numerals'),
((0x1D400, 0x1D7FF), u'字母和数字符号', u'Mathematical_Alphanumeric_Symbols'),
((0x1D800, 0x1DAAF), u'萨顿书写符号', u'Sutton_SignWriting'),
((0x1E800, 0x1E8DF), u'门地奇卡奎文', u'Mende_Kikakui'),
((0x1EE00, 0x1EEFF), u'阿拉伯字母数字符号', u'Arabic_Mathematical_Alphanumeric_Symbols'),
((0x1F000, 0x1F02F), u'麻将牌', u'Mahjong_Tiles'),
((0x1F030, 0x1F09F), u'多米诺骨牌', u'Domino_Tiles'),
((0x1F0A0, 0x1F0FF), u'扑克牌', u'Playing_Cards'),
((0x1F100, 0x1F1FF), u'带圈字母数字补充', u'Enclosed_Alphanumeric_Supplement'),
((0x1F200, 0x1F2FF), u'带圈表意文字补充', u'Enclosed_Ideographic_Supplement'),
((0x1F300, 0x1F5FF), u'杂项符号和象形文字', u'Miscellaneous_Symbols_And_Pictographs'),
((0x1F600, 0x1F64F), u'表情符号', u'Emotions'),
((0x1F650, 0x1F67F), u'装饰符号', u'Ornamental_Dingbats'),
((0x1F680, 0x1F6FF), u'交通和地图符号', u'Transport_And_Map_Symbols'),
((0x1F700, 0x1F77F), u'炼金术符号', u'Alchemical_Symbols'),
((0x1F780, 0x1F7FF), u'几何图形扩展', u'Geometric_Shapes_Extended'),
((0x1F800, 0x1F8FF), u'追加箭头-C', u'Supplemental_Arrows-C'),
((0x1F900, 0x1F9FF), u'補充符號和象形文字', u'Supplemental_Symbols_and_Pictographs'),
)

panel2 = (
((0x20000, 0x2A6DF), u'中日韓統一表意文字擴展B區', u'CJK_Unified_Ideographs_Extension_B'),
((0x2A700, 0x2B73F), u'中日韓統一表意文字擴展C區', u'CJK_Unified_Ideographs_Extension_C'),
((0x2B740, 0x2B81F), u'中日韓統一表意文字擴展D區', u'CJK_Unified_Ideographs_Extension_D'),
((0x2B820, 0x2CEAF), u'中日韓統一表意文字擴展E區', u'CJK_Unified_Ideographs_Extension_E'),
((0x2F800, 0x2FA1F), u'中日韓兼容表意文字增補', u'CJK_Compatibility_Ideographs_Supplement'),
)
panel14 = (
((0xE0000, 0xE007F), u'标签', u'Tags'),
((0xE0100, 0xE01EF), u'选择器变化补充', u'Variation_Selectors_Supplement'),
)

panel15 = (
    ((0xf0000, 0xffffd), u'私人使用区', u'Supplementary Private Use Area-A'),
)
panel16 = (
    ((0x100000, 0x10fffd), u'私人使用区', u'Supplementary Private Use Area-B'),
)

panels = (0, 1, 2, 14, 15, 16)
