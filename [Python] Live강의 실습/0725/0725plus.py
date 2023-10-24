# 혈액형 인원수 세기
# 결과 => {'A' : 3, 'B' : 3, 'O' : 3, 'AB' : 3}
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']


# solve 1 []

new_dict1 = {}
# blood_types을 순회하면서
for blood_type in blood_types:
    # 기존에 키가 이미 존재한다면,
    if blood_type in new_dict1:
        # 기존 키의 값을 +1 
        new_dict1[blood_type] += 1
    # 키가 존재하지 않는다면 (처음 설정되는 키)
    else :
        new_dict1[blood_type] = 1

print(new_dict1)



# solve 2 .get()      -> default가 존재

new_dict2 = {}
# blood_types을 순회하면서
for blood_type in blood_types:

    new_dict2[blood_type] = new_dict2.get(blood_type, 0) + 1     
    # 만약 new_dict.get(blood_type, 1) 로 한다면 아무것도 삽입되지 않아도 초기 값이 1로 설정되므로 최종 결과가 실제 인원수보다 1 많아짐 
        
print(new_dict2)



# solve 3 .setdefault()

new_dict3 = {}
# blood_types을 순회하면서
for blood_type in blood_types:
    new_dict3.setdefault(blood_type, 0)
    new_dict3[blood_type] += 1
print(new_dict3)