import chempy

def Balance_Equation(EL):
    LHElements=EL[0].split("+")
    RHElements=EL[1].split("+")       
    try:
        reactant,product=chempy.balance_stoichiometry(set(LHElements),set(RHElements))
        reactant=dict(reactant)
        product=dict(product)
        s=""
        c=0
        for i in reactant:
            s+=str(reactant[i])
            s+=i+" "
            c+=1
            if c!=len(reactant):
                s+="+"
            else:
                c=0
        s+=" ----> "
        for j in product:
            s+=str(product[j])
            s+=j+" "
            c+=1
            if c!=len(product):
                s+="+"
        print(s)
    except:
        print("Substances in reactant and product do not match or balance properly")

 
print("Welcome to the chemical equation balancer! Please give the reactants and products in the given prompts and when doing so, if the component contains brackets, please remove the brackets and distribute the power after it to the elements within the removed bracket")
LHE=input("Enter left hand side of the equation seperated by + operator: ")
RHE=input("Enter right hand side of the equation seperated by + operator: ")
EL=[LHE,RHE]
Balance_Equation(EL)