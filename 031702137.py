# -*- coding: utf-8 -*-
import json

def make_name(temp):
	return temp[2:temp.find(',')],temp[temp.find(',')+1:]

def make_phone(temp):
	st=-1
	while True:
		st=temp.find('1',st+1)
		en=st+10
		phone=temp[st:en+1]
		if phone.isdigit():
			break
	temp=temp[:st]+temp[en+1:]
	return phone,temp

def make_sheng(temp):
	vis=temp.find('省')
	if vis==-1:
		if temp[0:3] == "黑龙江":
			return temp[:3],temp[3:]
		else:
			return temp[:2],temp[2:]
	else:
		return temp[:vis],temp[vis+1:]

def make_city(temp):
	all_city=[ '玉溪', '保山', '昭通', '丽江', '普洱', '临沧', '贵阳', '六盘水', '遵义', '安顺', '成都', '绵阳', '德阳', '广元', '自贡', '攀枝花', '乐山', '南充', '内江', '遂宁', '广安', '泸州', '达州', '眉山', '乌鲁木齐', '克拉玛依', '拉萨 ', '银川', '石嘴山', '吴忠', '固原', '中卫', '呼和浩特', '包头', '乌海', '赤峰', '通辽', '鄂尔多斯', '呼伦贝尔', '巴彦淖尔', '乌兰察布', '南宁', '柳州', '桂林', '梧州', '北海', '崇左', '来宾', '贺州', '玉林', '百色', '河池', '钦州', '防城港', '贵港', '哈尔滨', '大庆', '齐齐哈尔', '佳木斯', '鸡西', '鹤岗', '双鸭山', '牡丹江', '伊春', '七台河', '黑河', '绥化', '长春', '吉林', '四平', '辽源', '通化', '白山', '松原', '白城', '沈阳', '大连', '鞍山', '抚顺', '本溪', '丹东', '锦州', '营口', '阜新', '辽阳', '盘锦', '铁岭', '朝阳', '葫芦岛', '石家庄', '唐山', '邯郸', '秦皇岛', '保定', '张家口', '承德', '廊坊', '沧州', '衡水', '邢台', '济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '莱芜', '临沂', '德州', '聊城', '菏泽', '滨州', '南京', '镇江', '常州', '无锡', '苏州', '徐州', '连云港', '淮安', '盐城', '扬州', '泰州', '南通', '宿迁', '合肥', '蚌埠', '芜湖', '淮南', '亳州', '阜阳', '淮北', '宿州', '滁州', '安庆', '巢湖', '马鞍山', '宣城', '黄山', '池州', '铜陵', '杭州', '嘉兴', '湖州', '宁波', '金华', '温州', '丽水', '绍兴', '衢州', '舟山', '台州', '福州', '厦门', '泉州', '三明', '南平', '漳州', '莆田', '宁德', '龙岩', '广州', '深圳', '汕头', '惠州', '珠海', '揭阳', '佛山', '河源', '阳江', '茂名', '湛江', '梅州', '肇庆', '韶关', '潮州', '东莞', '中山', '清远', '江门', '汕尾', '云浮', '海口', '三亚', '昆明', '曲靖','宜宾', '雅安', '资阳', '长沙', '株洲', '湘潭', '衡阳', '岳阳', '郴州', '永州', '邵阳', '怀化', '常德', '益阳', '张家界', '娄底 ', '武汉', '襄樊', '宜昌', '黄石', '鄂州', '随州', '荆州', '荆门', '十堰', '孝感', '黄冈', '咸宁', '郑州', '洛阳', '开封', '漯河', '安阳', '新乡', '周口', '三门峡', '焦作', '平顶山', '信阳', '南阳', '鹤壁', '濮阳', '许昌', '商丘', '驻马店', '太原', '大同', '忻州', '阳泉', '长治', '晋城', '朔州', '晋中', '运城', '临汾', '吕梁', '西安', '咸阳', '铜川', '延安', '宝鸡', '渭南', '汉中', '安康', '商洛', '榆林', '兰州', '天水', '平凉', '酒泉', '嘉峪关', '金昌', '白银', '武威', '张掖', '庆阳', '定西', '陇南', '西宁', '南昌', '九江', '赣州', '吉安', '鹰潭', '上饶', '萍乡', '景德镇', '新余', '宜春', '抚州','延边朝鲜族自治州', '恩施土家族苗族自治州', '湘西土家族苗族自治州', '临夏回族自治州', '甘南藏族自治州', '甘孜藏族自治州', '凉山彝族自治州', '阿坝藏族羌族自治州', '黔东南苗族侗族自治州', '黔南布依族苗族自治州', '黔西南布依族苗族自治州', '昌吉回族自治州', '伊犁哈萨克自治州', '博尔塔拉蒙古自治州', '巴音郭楞蒙古自治州', '黄南藏族自治州', '海北藏族自治州', '海南藏族自治州', '果洛藏族自治州', '玉树藏族自治州', '海西蒙古族藏族自治州', '迪庆藏族自治州', '楚雄彝族自治州', '大理白族自治州', '怒江傈僳族自治州', ' 西双版纳傣族自治州', '文山壮族苗族自治州', '德宏傣族景颇族自治州', '红河哈尼族彝族自治州', '克孜勒苏柯尔克孜自治州']
	city=''
	for i in all_city:
		if temp.find(i)!=-1:
			l=len(i)
			city=temp[:l]
			temp=temp[l:]
			break
	if temp[0]=='市':
		temp=temp[1:]
	if city[-1]!='州':
		city+='市'
	return city,temp

def make_three(temp):
	vis=temp.find('市')
	if vis==-1:
	   vis=temp.find('县')
	if vis==-1:
		vis=temp.find('区')
	if vis==-1:
		return '',temp
	else:
		return temp[:vis+1],temp[vis+1:]
		
def make_four(temp):
	vis=temp.find('道')
	if vis==-1:
	   vis=temp.find('镇')
	if vis==-1:
		vis=temp.find('乡')
	if vis==-1:
		return '',temp
	else:
		return temp[:vis+1],temp[vis+1:]

def make_five(temp):
	vis=temp.find('路')
	if vis==-1:
		return '',temp
	else:
		return temp[:vis+1],temp[vis+1:]
def make_six(temp):
	vis=temp.find('号')
	if vis==-1:
		return '',temp
	else:
		return temp[:vis+1],temp[vis+1:]
ans={}
address=input()
flag=address[0]
#截取姓名
ans['姓名'],new_address=make_name(address)

#截取电话
ans['手机'],new_address=make_phone(new_address)

#截取省份和城市
detail_address=[]
province,new_address=make_sheng(new_address)
if province=='北京'or province=='上海'or province=='重庆'or province=='天津':
	city=province+'市'
	if new_address[0]=='市':
		new_address=new_address[1:]
else:
	if province=='宁夏':
		province+='回族自治区'
		if new_address[0:5]=='回族自治区':
			new_address=new_address[5:]
	
	elif province=='广西':
		province+='壮族自治区'
		if new_address[0:5]=='壮族自治区':
			new_address=new_address[5:]
	elif province=='新疆':
		province+='维吾尔自治区'
		if new_address[0:6]=='维吾尔自治区':
			new_address=new_address[6:]
	elif province=='内蒙古'or province=='西藏':
		province+='自治区'
		if new_address[0:3]=='自治区':
			new_address=new_address[3:]
	else:
		province+='省'
	city,new_address=make_city(new_address)
detail_address.append(province)
detail_address.append(city)
#截取剩下五级地址
three,new_address=make_three(new_address)
detail_address.append(three)
four,new_address=make_four(new_address)
detail_address.append(four)
if flag=='2':
	five,new_address=make_five(new_address)
	detail_address.append(five)
	six,new_address=make_six(new_address)
	detail_address.append(six)
seven=new_address[:-1]
detail_address.append(seven)

ans['地址']=detail_address
#print(ans)
print(json.dumps(ans))
