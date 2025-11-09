#
# age = int(input("How old are you?"))
# ismember = input("Are you member? (yes/no)").lower()
#
# if age < 18:
#     print("you get a 20% discount!")
# elif 18 <= age < 25 and ismember == "yes":
#     print("you get a 15% discount!")
# elif 18 <= age <= 25 and ismember == "no":
#     print("you get a 5% discount! ")
# elif age > 25 and ismember == "yes":
#     print("you get a 10% discount!")
# else:
#     print("you do not get a discount")

#
# age = int(input("How old are you?"))
# average = int(input("What is your average?"))
# scolarship = input("Do you have scolarship (yes/no) ").lower()
# hasScolarship = scolarship == "yes"
#
# if age < 12:
#     if average >= 90:
#         if scolarship:
#             print("you are a child with excellent perfomance with scolarship!")
#         else:
#             print("you are a child with poor performance without scolarship!")
#     elif 75 <= average <= 90:
#         if scolarship:
#             print("you are a child with good perfomance with scolarship!")
#         else:
#             print("you are a child with good perfomance without scolarship!")
#     elif 60 <= average <= 75:
#         if scolarship:
#             print("you are a child with average perfomance with scolarship!")
#         else:
#             print("you are a child with average perfomance without scolarship!")
#     elif average < 60:
#         if scolarship:
#             print("you are a child with poor perfomance with scolarship!")
#         else:
#             print("you are a child with poor perfomance without scolarship!")
# elif 12 <= age <= 17:
#     if average >= 90:
#         if scolarship:
#             print("you are a teenager with excellent perfomance with scolarship!")
#         else:
#             print("you are a teenager with poor performance without scolarship!")
#     elif 75 <= average <= 90:
#         if scolarship:
#             print("you are a teenager with good perfomance with scolarship!")
#         else:
#              print("you are a teenager with good perfomance without scolarship!")
#     elif 60 <= average <= 75:
#         if scolarship:
#             print("you are a teenager with average perfomance with scolarship!")
#         else:
#             print("you are a teenager with average perfomance without scolarship!")
#     elif average < 60:
#         if scolarship:
#             print("you are a teenager with poor perfomance with scolarship!")
#         else:
#             print("you are a teenager with poor perfomance without scolarship!")
# elif age >= 18:
#     if average >= 90:
#         if scolarship:
#             print("you are a adult with excellent perfomance with scolarship!")
#         else:
#             print("you are a adult with poor performance without scolarship!")
#     elif 75 <= average <= 90:
#         if scolarship:
#             print("you are a adult with good perfomance with scolarship!")
#         else:
#              print("you are a adult with good perfomance without scolarship!")
#     elif 60 <= average <= 75:
#         if scolarship:
#             print("you are a adult with average perfomance with scolarship!")
#         else:
#             print("you are a adult with average perfomance without scolarship!")
#     elif average < 60:
#         if scolarship:
#             print("you are a adult with poor perfomance with scolarship!")
#         else:
#             print("you are a adult with poor perfomance without scolarship!")
# else:
#     print("We haven't nothing for you")

# age = int(input("How old are you?"))
# average = int(input("What's your average?"))
# scolarship = input("Do you have scolarship? (yes?no) ").lower()
# has_Scolarship = scolarship == "Yes"
#
# if age < 12:
#     age_group = "child"
# elif 12 <= age <= 17:
#     age_group = "teenager"
# else:
#     age_group = "adult"
#
# if average >= 90:
#     performance = "excellent"
# elif 75 <= average <= 90:
#     performance = "good"
# elif 60 <= average <= 75:
#     performance = "average"
# else:
#     performance = "poor"
#
# message = f"you are a {age_group} with {performance} performance"
#
# if has_Scolarship:
#     message += " with scolarship"
# else:
#     message += " without scolarship"
#
# print(message)


# age = int(input("How old are you?"))
# student = input("Are you student? (yes/no)")
# member = input("Are you member of the cinema club? (yes/no)").lower()
#
# is_Student = student == "yes"
# is_Member = member == "yes"
#
# if age < 12:
#     discount = 50
# elif 12 <= age <= 25 and is_Student:
#     discount = 25
# else:
#     discount = "0"
#
# if is_Member:
#     discount += 10
#
# print(f"Your total discount is {discount}%")

# age = int(input("How old are you?"))
# monthly_income = int(input("What's your monthly income? (Example: 10000) "))
# crediHistory = input("What's your credit history like? (excellent/good/fair/poor)").lower()
# activeDebts = input("Do you have any active debts? (yes/ no)").lower()
# has_Active_Debts = activeDebts == "yes"
#
# if age < 18:
#     loan_description = "Loan not available for minors"
# elif age > 65:
#     loan_description = "Loan approved for $10,000!"
# else:
#     loan_description = "Loan approved"
#
# if has_Active_Debts:
#     if monthly_income > 5000 and crediHistory == "excellent":
#         loan_description = "Loan approved!"
#
# if has_Active_Debts:
#     loan_description = "Loan denied due to insufficient credit history"
#
# if not has_Active_Debts:
#     if monthly_income >= 8000 and crediHistory == "excellent" or crediHistory == "good":
#         loan_description += " for $50000"
#     elif 4000 <= monthly_income <= 7999 and crediHistory == "fair":
#         loan_description += " for $20000"
# else:
#     loan_description = "Loan denied due to insufficient credit history"


# print(loan_description)

# age = int(input("How old are you? "))
# monthly_income = int(input("What's your monthly income? (Example: 10000) "))
# credit_history = input("What's your credit history like? (excellent/good/regular/poor) ").lower()
# active_debts = input("Do you have any active debts? (yes/no) ").lower()
#
# has_active_debts = active_debts == "yes"
#
# # --- Evaluación ---
# if age < 18:
#     loan_description = "❌ Loan not available for minors."
# elif age > 65:
#     loan_description = "✅ Loan approved for $10,000 (senior plan)."
# else:
#     if has_active_debts:
#         if monthly_income > 5000 and credit_history == "excellent":
#             loan_description = "✅ Loan approved for $15,000 (with active debts)."
#         else:
#             loan_description = "❌ Loan denied due to active debts."
#     else:
#         if monthly_income >= 8000 and (credit_history == "excellent" or credit_history == "good"):
#             loan_description = "✅ Loan approved for $50,000."
#         elif 4000 <= monthly_income <= 7999 and credit_history in ("excellent", "good", "regular"):
#             loan_description = "✅ Loan approved for $20,000."
#         else:
#             loan_description = "❌ Loan denied due to insufficient income or poor credit history."
#
# print("\n" + loan_description)


# nombre = input("Por favor, ingrese su nombre:").lower()
# monto_total = int(input("Ingrese el monto total de compras en el último año. Ejemplo (5000):"))
# anosAntiguedad = int(input("Ingrese los años de antiguidad como cliente. Ejemplo (6/7/9) años:"))
# metodoPago = input("Por favor, ingrese su metodo de pago. Ejemplo (Tarjeta/Paypal/Transferencia)").lower()
#
#
# if monto_total < 2000:
#     tipoCliente = "Cliente Nuevo"
# elif  2000 <= monto_total <= 5000:
#     tipoCliente = "Cliente Frecuente"
# else:
#     tipoCliente = "Cliente Premium"
#
# if  anosAntiguedad < 2:
#     tipoFidelidad = "Baja"
# elif 2 <= anosAntiguedad <= 5:
#     tipoFidelidad = "Media"
# else:
#     tipoFidelidad = "Alta"
#
# if metodoPago == "tarjeta":
#     recomendacion = "Obtén un 10% de descuento si activas pagos automáticos."
# elif metodoPago == "paypal":
#     recomendacion = "Recuerda vincular tu cuenta bancaria para evitar límites."
# elif metodoPago == "transferencia":
#     recomendacion = "Te recomendamos probar PayPal para pagos más rápidos."
#acion = input("Evaluación de desempeño (A/B/C/D): ").strip().upper()

# bono = ""
# if tipoCliente == "Cliente Premium" and tipoFidelidad == "Alta":
#     bono = "Bonificación especial: envío gratis todo el año!"
#
# print("\n --- PERFIL DEL CLIENTE ---")
# print(f"Nombre: {nombre}")
# print(f"Tipo de Cliente: {tipoCliente}")
# print(f"Nivel de Fidelidad: {tipoFidelidad}")
# print(f"Método de pago: {metodoPago}")
# print(f"Recomendación: {recomendacion}")
# if bono:
#     print(bono)
# Lista para guardar los empleados
empleados = []

# Solicitar cantidad
n = int(input("¿Cuántos empleados desea registrar?: "))

for i in range(n):
    print(f"\n--- Empleado #{i+1} ---")
    nombre = input("Nombre del empleado: ").strip().title()
    puesto = input("Puesto (junior/senior/lider): ").strip().lower()
    experiencia = int(input("Años de experiencia: "))
    evaluacion = input("Evaluación de desempeño (A/B/C/D): ").strip().upper()

    # Bonificación base según puesto y evaluación
    if puesto == "junior":
        if evaluacion == "A":
            bono = 10
        elif evaluacion == "B":
            bono = 7
        elif evaluacion == "C":
            bono = 4
        else:
            bono = 0
    elif puesto == "senior":
        if evaluacion == "A":
            bono = 15
        elif evaluacion == "B":
            bono = 10
        elif evaluacion == "C":
            bono = 5
        else:
            bono = 0
    elif puesto == "lider":
        if evaluacion == "A":
            bono = 20
        elif evaluacion == "B":
            bono = 12
        elif evaluacion == "C":
            bono = 7
        else:
            bono = 0
    else:
        print("⚠️ Puesto no reconocido. Se asigna bonificación 0%.")
        bono = 0

    # Bono adicional por antigüedad
    if experiencia > 5:
        bono += 3

    # Nivel del empleado según bonificación total
    if bono >= 18:
        nivel = "Excelente"
    elif bono >= 10:
        nivel = "Bueno"
    elif bono >= 5:
        nivel = "Regular"
    else:
        nivel = "Bajo Rendimiento"

    # Agregar a la lista
    empleados.append({
        "nombre": nombre,
        "puesto": puesto,
        "evaluacion": evaluacion,
        "bono": bono,
        "nivel": nivel
    })

# Mostrar resumen
print("\n===== RESUMEN DE EMPLEADOS =====")
for e in empleados:
    print(f"\nEmpleado: {e['nombre']}")
    print(f"Puesto: {e['puesto'].capitalize()}")
    print(f"Evaluación: {e['evaluacion']}")
    print(f"Bonificación total: {e['bono']}%")
    print(f"Nivel: {e['nivel']}")


