def complexNumberMultiply(a, b):
  
  a_index = a.index('+')
  b_index = b.index('+')
  
  real_a = int(a[0:a_index])
  image_a = int(a[a_index+1:-1])
  print(image_a)
  real_b = int(b[0:b_index])
  image_b = int(b[b_index+1:-1])
  print(image_b)

  
  result_real = str(real_a * real_b - image_a * image_b)
  result_img  = str(real_a * image_b + real_b * image_a)
  return result_real+ '+' +result_img +'i'

a = '3+-1i'
b = '99+99i'

print(complexNumberMultiply(a, b))