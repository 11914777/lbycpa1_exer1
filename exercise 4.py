#Formula selection screen
while True:
    print("\n********** Formula Selection Screen **********\n")
    print("Select a formula from the formula selection screen. ")

    print("[1] Centripital Force Equation")
    print("[2] Second Kinematics Equation")
    print("[0] Quit")

#accept formula of choice from user
    choice = int(input("\nSelect the corresponding number of the formula that you want to choose:\n "))

#Variable selection screen and computation
    #For Centripital Force Equation
    if choice == 1:

        while True:
            print("\n********** Variable Selection Screen **********\n")
            print("Select variable from the Centripital Force Equation. ")

            print("[1] Fnet = Net Force")
            print("[2] m = mass")
            print("[3] v = velocity")
            print("[4] R = radius")
            print("[0] Go back to Formula Selection Screen. ")

            var_cf = int(input("\nSelect the corresponding number of the variable that you want to compute for in the equation.\n "))

            #accept input variable
            if var_cf == 1:
                m = float(input("Input the mass of the object. "))
                v = float(input("Input the velocity of the object. "))
                r = float(input("Input the radius of the object. "))
                #Equation
                fn = (m * (v**2)) / r

                print("\nThe Net Force is:\n", fn)

            if var_cf == 2:
                fn = float(input("Input the Net Force. "))
                v = float(input("Input the velocity of the object. "))
                r = float(input("Input the radius of the object. "))
                #Equation derived
                m = fn*r / v**2

                print("\nThe mass is:\n", m)
                    
            if var_cf == 3:
                fn = float(input("Input the Net Force. "))
                m = float(input("Input the mass of the object. "))
                r = float(input("Input the radius of the object. "))
                #Equation derived
                v = (fn*r / m )**0.5

                print("\nThe velocity of the object is:\n", v)

                    
            if var_cf == 4:
                fn = float(input("Input the Net Force. "))
                m = float(input("Input the mass of the object. "))
                v = float(input("Input the velocity of the object. "))
                #Equation derived
                r = (m * (v**2)) / fn

                print("\nThe radius of the circle is:\n", r)

            if var_cf == 0:
                break

    #For First Kinematics Equation
    if choice == 2:

        while True:
            print("\n********** Variable Selection Screen **********\n")
            print("Select variable from the First Kinematics Equation. ")
            
            print("[1] Vox = Initial velocity")
            print("[2] Vx = Final velocity")
            print("[3] a = Acceleration")
            print("[4] t = Time ellapsed")
            print("[0] Go back to Formula Selection Screen. ")

            var_fke = int(input("\nSelect the corresponding number of the variable that you want to compute for in the equation.\n "))

            #accept input variable
            if var_fke == 1:
                vx = float(input("Input the final velocity of the object. "))
                acc = float(input("Input the acceleration. "))
                t = float(input("Input the time ellapsed. "))
                #Equation derived
                vox = vx - (acc * t)

                print("\nThe initial velocity is:\n", vox)

            if var_fke == 2:
                vox = float(input("Input the initial velocity of the object. "))
                acc = float(input("Input the acceleration. "))
                t = float(input("Input the time ellapsed. "))
                #Equation
                vx = vox + (acc * t)
                 
                print("\nThe final velocity is:\n", vx)
                    
            if var_fke == 3:
                vox = float(input("Input the initial velocity of the object. "))
                vx = float(input("Input the final velocity of the object. "))
                t = float(input("Input the time ellapsed. "))
                #Equation derived
                acc = (vx - vox) / t
                 
                print("\nThe acceleration is:\n", acc)

            if var_fke == 4:
                vox = float(input("Input the initial velocity of the object. "))
                vx = float(input("Input the final velocity of the object. "))
                acc = float(input("Input the acceleration. "))
                #Equation deriveds
                t = (vx - vox) / acc
                 
                print("\nThe time ellapsed is:\n", t)

            if var_fke == 0:
                break

    #For the program to quit
    if choice == 0:
        break 