import json

# Dán toàn bộ dữ liệu của bạn vào đây:
vocab_data = """
study	n, v	/ˈstʌdi/	học tập, nghiên cứu	Study = học
stunned	v	/stʌnd/	choáng váng, sửng sốt	Sờ tan nát tin tức → quá choáng váng
subtle	adj	/ˈsʌtl/	tinh tế, khôn khéo	Sắp tê → cảm giác mơ hồ, tinh vi
subtract	v	/səbˈtrækt/	trừ đi	Sub = dưới + tract = kéo → kéo xuống = trừ
success	n	/səkˈses/	thành công	Sờ cát xét kỹ lưỡng mới thành công
suggest	v	/səˈdʒest/	đề nghị, gợi ý	Sợ chết nên gợi ý cách sống an toàn hơn
supervise	v	/ˈsuːpəvaɪz/	giám sát, trông coi	Sờ bà vai khi đang giám sát công việc
support	n, v	/səˈpɔːt/	hỗ trợ	Sờ bồ → được ủng hộ, hỗ trợ
surge	v	/sɜːdʒ/	trào lên, tăng mạnh	Sợ dơ vì nước trào lên
surplus	n	/ˈsɜːpləs/	thặng dư, số dư	Sờ plus – cộng thêm → tức là có số dư
surprising	adj	/səˈpraɪzɪŋ/	ngạc nhiên	Sờ phải rắn → giật mình bất ngờ
sustain	v	/səˈsteɪn/	duy trì, giữ vững	Sờ sờ tên mãi không quên → duy trì lâu dài
swift	adj, adv	/swɪft/	nhanh chóng, mau lẹ	Sờ wifi siêu nhanh
symbolize	v	/ˈsɪmbəlaɪz/	tượng trưng	Sim bồ like hình trái tim → biểu tượng tình yêu
talkative	adj	/ˈtɔːkətɪv/	nói nhiều, lắm chuyện	Tó cái tivi để bớt nói nhiều
tall	adj	/tɔːl/	cao	Tò cổ lên nhìn → vì quá cao
tame	adj, v	/teɪm/	thuần hóa, ngoan ngoãn	Thầy m dạy thú biết vâng lời → thuần hóa
tandem	n	/ˈtændəm/	xe hai ngựa/xe hai yên nối tiếp	Tán đầm trên xe đôi → ngồi liền nhau
tangible	adj	/ˈtændʒəbl/	hữu hình, sờ được	Tán cho bồ vật gì đó sờ được
taut	adj	/tɔːt/	căng, không chùng	Tô thắt dây cho căng
tavern	n	/ˈtævən/	quán rượu	Té vấp lên rượn vì say ở quán rượu
temper	n	/ˈtempə(r)/	tính khí, tâm tính	Tém bơ để giữ bình tĩnh
temporary	adj	/ˈtempərəri/	tạm thời	Tạm bỏ rơi vì tạm thời không cần
tender	adj	/ˈtendə(r)/	mềm, dịu, nhạy cảm	Tê nên đỡ nhẹ → vì mềm yếu, nhạy cảm
tenet	n	/ˈtenɪt/	nguyên lý, giáo lý	Tén nít trong chùa vì làm trái giáo lý
tense	adj, v	/tens/	căng thẳng	Tén xệ → người căng cứng vì lo lắng
terrible	adj	/ˈterəbl/	kinh khủng, khủng khiếp	Tê rợn bồ → vì chuyện kinh khủng
thoughtless	adj	/ˈθɔːtləs/	vô tâm, không suy nghĩ	Thôi lết luôn vì bị người vô tâm làm đau
thrifty	adj	/ˈθrɪfti/	tiết kiệm, tằn tiện	Thích rít tý sữa thôi → tiết kiệm quá mức
thrive	v	/θraɪv/	phát đạt, thịnh vượng	Thời rì vè thành công → phát triển thịnh vượng
thumping	adj, adv	/ˈθʌmpɪŋ/	rất to, rất lớn	Thăm ping mạng rất lớn → tốc độ cao
tight	adj	/taɪt/	chặt, bó	Tay tét vì đồ quá chặt
timely	adj	/ˈtaɪmli/	kịp thời, đúng lúc	Time lì → vẫn đến đúng lúc
timid	adj	/ˈtɪmɪd/	nhút nhát	Tim yếu nên rút lui nhút nhát
tip	n, v	/tɪp/	mẹo, đầu nhọn, boa tiền	Tip = tiền boa ở quán
toilet	n	/ˈtɔɪlət/	nhà vệ sinh	Toi lẹt = nhà toilet
traffic	n	/ˈtræfɪk/	giao thông	Tránh phít → kẹt giao thông
tragic	adj	/ˈtrædʒɪk/	bi kịch	Trái tim giật mạnh vì chuyện bi kịch
tranquil	adj	/ˈtræŋkwɪl/	yên bình, yên tĩnh	Trang quỳnh → cô gái dịu dàng, yên tĩnh
tranquility	n	/træŋˈkwɪləti/	sự yên bình, sự thanh thản	Trang quý lì ti – rất yên bình, không bị làm phiền
transform	v	/trænsˈfɔːm/	biến đổi	Transformers = biến hình
transitory	adj	/ˈtrænsətri/	ngắn ngủi, tạm thời	Tranh sơ thôi → chỉ là tạm thời
tremble	v	/ˈtrembl/	run rẩy	Trẹm bồ vì run sợ
triumph	n, v	/ˈtraɪəmf/	chiến thắng	Try ấm → cố gắng và thành công
trivial	adj	/ˈtrɪviəl/	tầm thường, không quan trọng	Trí vị ảo → không có thật → tầm thường
trustworthy	adj	/ˈtrʌstwɜːði/	đáng tin	Trách sờ thề → người đáng tin
ultrasound	n	/ˈʌltrəsaʊnd/	siêu âm	Ultra sound = âm siêu mạnh
umbrella	n	/ʌmˈbrelə/	cái ô	Ùm bơi ra mà không có ô che mưa
unchanging	adj	/ʌnˈtʃeɪndʒɪŋ/	không thay đổi	Ăn chay hoài → tính không đổi
unconquerable	adj	/ʌnˈkɒŋkərəbl/	không thể bị đánh bại	Ăn con cá rồ cũng không khuất phục → rất kiên cường
uncooked	adj	/ʌnˈkʊkt/	chưa nấu	Ăn cút sống → vì còn chưa nấu chín
unfortunate	adj	/ʌnˈfɔːtʃənət/	không may	Ăn phở chưa nấu → xui xẻo đau bụng
unimportant	adj	/ˌʌnɪmˈpɔːtnt/	không quan trọng	Ăn im không có vai trò gì → không quan trọng
unintelligent	adj	/ˌʌnɪnˈtelɪdʒənt/	không thông minh	Ăn in tê liền → do không hiểu gì cả
unkind	adj	/ʌnˈkaɪnd/	độc ác, không tử tế	Ăn kẹo in đá → người xấu tính
unlucky	adj	/ʌnˈlʌki/	không may mắn	Ăn lạc kỳ → ăn mà xui xẻo
unoccupied	adj	/ʌnˈɒkjupaɪd/	trống, không có người	Ăn óc chua → thấy bỏ trống, không ai dùng
unpretentious	adj	/ˌʌnpriˈtenʃəs/	khiêm tốn, không khoe khoang	Ăn bánh trứng vẫn khiêm tốn, không khoe
unrelated	adj	/ˌʌnrɪˈleɪtɪd/	không liên quan	Ăn rì lết nhưng không liên quan gì
unstoppable	adj	/ʌnˈstɒpəbl/	không thể ngăn lại	Ăn stop bồ → nhưng không dừng lại được
unusual	adj	/ʌnˈjuːʒuəl/	bất thường	Ăn nhiều dù dở → thấy bất thường
unwilling	adj	/ʌnˈwɪlɪŋ/	không muốn, miễn cưỡng	Ăn willy nilly → ăn miễn cưỡng
update	v	/ˈʌpdeɪt/	cập nhật	Up date → nâng cấp, cập nhật thời gian
upstanding	adj	/ʌpˈstændɪŋ/	chính trực, thẳng thắn	Up stand → người đứng thẳng, không gian lận
urge	n, v	/ɜːdʒ/	thúc giục, ham muốn	Ơ giờ phải đi → cảm giác thúc giục
urgent	adj	/ˈɜːdʒənt/	khẩn cấp	Ơ giờ nên làm liền vì khẩn cấp
utilize	v	/ˈjuːtəlaɪz/	tận dụng, sử dụng	You tới lại để dùng lại đồ cũ
vacant	adj	/ˈveɪkənt/	trống rỗng	Về cần gì đâu → nhà trống rỗng
vague	adj	/veɪg/	mơ hồ, không rõ	Về gấp nhưng vẫn mơ hồ
valiant	adj	/ˈvæliənt/	dũng cảm	Vào liền chiến trận → rất anh dũng
valour	n	/ˈvælə(r)/	sự dũng cảm	Vào lửa mà không sợ → thể hiện dũng cảm
vanquish	v	/ˈvæŋkwɪʃ/	đánh bại	Văng quýt vô địch → đánh bại hết đối thủ
variety	n	/vəˈraɪəti/	sự đa dạng	Vờ ra i ti đủ thứ → quá đa dạng
vary	v	/ˈveəri/	thay đổi	Về rồi lại thay đổi
vast	adj	/vɑːst/	bao la, rộng lớn	Vác đi khắp nơi vì rộng bao la
vendor	n	/ˈvendə(r)/	người bán hàng	Về đợt bán hàng tiếp theo với vendor
verdict	n	/ˈvɜːdɪkt/	phán quyết	Vỡ điếc vì nghe lời phán quyết shock
versatile	adj	/ˈvɜːsətaɪl/	linh hoạt, đa năng	Vợ sờ tai cũng giỏi → người đa tài, linh hoạt
viable	adj	/ˈvaɪəbl/	khả thi	Vài ớt bồ cũng bán được → kế hoạch khả thi
victory	n	/ˈvɪktəri/	chiến thắng	Vít tới đi để giành chiến thắng
vigorous	adj	/ˈvɪɡərəs/	mạnh mẽ, sôi nổi	Vì gà rớt → chạy mạnh mẽ nhặt lại
vile	adj	/vaɪl/	ghê tởm, đáng khinh	Vãi thật, thấy ghê tởm
violent	adj	/ˈvaɪələnt/	bạo lực, hung dữ, dữ dội	Vái lần cuối vì bị đánh quá bạo lực
virtuous	adj	/ˈvɜːtʃuəs/	có đạo đức, có phẩm hạnh	Vợ chưa sờ ai → rất có đức 
voluntary	adj	/ˈvɒləntri/	tự nguyện	Vào lộn tiệm giúp đỡ người khác → tự nguyện
vulgar	adj	/ˈvʌlɡə(r)/	thô tục, thiếu văn hóa	Văng gạch bậy → nói tục tĩu
waiver	n	/ˈweɪvə(r)/	miễn trừ, từ bỏ	Về vợ ký từ bỏ quyền lợi
wardrobe	n	/ˈwɔːdrəʊb/	tủ quần áo	Woa đồ rớt đầy trong tủ quần áo
warlike	adj	/ˈwɔːlaɪk/	hiếu chiến, thuộc về chiến tranh	Woa lại đánh nhau nữa rồi → người hiếu chiến
wealthy	adj	/ˈwelθi/	giàu, giàu có	Well thì nhà giàu lắm
weird	adj	/wɪəd/	kỳ lạ, khác thường, khó hiểu	Quý ợt quá → người kỳ quái
wide	adj	/waɪd/	rộng, rộng lớn	Why đường này rộng thế
willingly	adv	/ˈwɪlɪŋli/	sẵn lòng, vui lòng, tự nguyện	Will Linh luôn làm tự nguyện
win	n, v	/wɪn/	chiến thắng, thắng cuộc	Win = chiến thắng (quá phổ biến rồi)
wisecrack	n, v	/ˈwaɪzkræk/	nói lém lỉnh, nói đùa	Why cười ác → nói lém lỉnh làm người khác bật cười
withdraw	v	/wɪðˈdrɔː/	rút khỏi, rút lui	Rút đồ về = rút lui khỏi trận
withstand	v	/ˌwɪðˈstænd/	chịu đựng, chống lại	With stand → đứng vững cùng ai = chịu đựng, chống lại
woe	n	/wəʊ/	sự đau buồn, nỗi phiền muộn	Woa buồn quá, chuyện này thật woe
worn	adj	/wɔːn/	mòn, hao mòn	Worn-out = đã mòn rồi
yell	n, v	/jel/	hét, la hét, tiếng hét	Yêu quá mà bị cắm sừng → la hét
yield	n	/jiːld/	năng suất, sản lượng; nhường đường	Giữ lúa = có năng suất, cũng có thể yield = nhường đường

"""

# Chuyển thành danh sách các từ điển
entries = []
for line in vocab_data.strip().split('\n'):
    parts = line.split('\t')
    if len(parts) == 5:
        vocab, pos, ipa, meaning, mnemonic = parts
        entries.append({
            "Từ vựng": vocab,
            "Phiên âm": ipa,
            "Loại từ": pos,
            "Ý nghĩa": meaning,
            "Cách nhớ nhanh": mnemonic
        })

# Chia thành các phần 20 từ và lưu ra file
for i in range(0, len(entries), 20):
    chunk = entries[i:i + 20]
    filename = f'part10-{i // 20 + 1}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(chunk, f, ensure_ascii=False, indent=4)

print("✅ Đã tạo các file: part1.json, part2.json, ...")
