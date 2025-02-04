def data_types():
    var1 = 1
    var2 = 'hello'
    var3 = 3.14
    var4 = True
    var5 = [1, 2, 3]
    var6 = {'key1': 'value1', 'key2': 'value2'}
    var7 = (1, 2, 3)
    var8 = {12, 'hello', True}

    print(f"[{type(var1).__name__}, {type(var2).__name__}, {type(var3).__name__}, {type(var4).__name__}, {type(var5).__name__}, {type(var6).__name__}, {type(var7).__name__}, {type(var8).__name__}]")

if __name__ == "__main__":
    data_types()
else:
    print("function not found!")