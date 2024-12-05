'''
dictionary comphrehension = create dictionary using an expression
                            can replace for loops and certain lambda functions

                            dictionary {key: expression for (key,value) in iretable }
                            dictionary {key: expression for (key,value) in iretable if conditional}
                            dictionary {key: (if/else) for (key,value) in iretable }
                            dictionary {key: function(value) for (key,value) in iretable }
                            
'''
def check_temp(Value):
    if Value <= 32:
        return ('dingin')
    elif 69 <= Value <= 100:
        return ('panas')
    else:
        return ('cold')
suhu_kota_di_F = {'bandung':100,'jakarta':70,'semarang':32,'surabaya':67}

suhu_kota_di_c = {key: ((Value-32)*5/9) for (key,Value) in suhu_kota_di_F.items()}
print(suhu_kota_di_c)


weather = {'bandung':'cloudy','jakarta':'sunny','semarang':'cloudy','surabaya':'sunny'}
sunny_weather = {key: value for (key,value) in weather.items() if value == 'sunny'}
print(sunny_weather)

#contoh if else dictionary comprehension
suhu_kota = {'bandung':100,'jakarta':70,'semarang':32,'surabaya':67}
suhu = {key: ('dingin' if value <= 32 else 'panas') for (key,value) in suhu_kota.items()}
print (suhu)

#contoh function dictionary comprehension
suhu_kotaa= {'bandung':100,'jakarta':70,'semarang':32,'surabaya':67}
desc_kota = {key: check_temp(Value) for (key,Value) in suhu_kotaa.items()}
