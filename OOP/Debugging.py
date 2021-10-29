# Membuat Class
class classA:
    pass

# Membuat instance
instance1= classA()
# Membuat atribut dari instance, tidak perlu didefinisikian sebelumnya di classA
instance1.name="uwau"
print(instance1.name)

# Untuk membantu debug kita bisa menggunakan fungsi help() dan __dict__
print("Ini print memakai magic method __dict__ :",instance1.__dict__)

print(help(instance1))