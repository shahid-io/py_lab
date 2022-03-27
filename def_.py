def outer_func(s):
    
    def inner_func():
        print(f"Hello,{s}")
    
    inner_func()

outer_func("world!")


