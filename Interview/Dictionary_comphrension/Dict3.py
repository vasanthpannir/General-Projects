scores = {'John': 85, 'Emily': 92, 'Anna': 78, 'Mike': 89}
result = {k:('pass' if v>=80 else 'fail')for k,v in scores.items()}
print(result)