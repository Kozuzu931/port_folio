def BMI(old,hight,weight):
  BMIresult=float(weight)/float((hight**2))
  if old>=45:
    if BMIresult>=22.0:
      print("心臓病のリスクが高いです。")
    elif BMIresult<22.0:
      print("心臓病のリスクは中です。")
  elif  old<45:
      if BMIresult>=22.0:
        print("心臓病のリスクは中です。")
      elif BMIresult<22.0:
        print("心臓病のリスクは低いです。")
