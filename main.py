def main():
    print()
    # Ask the user for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    print()
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = weight / (height ** 2)

    print()

    # Determine BMI category and give feedback
    if bmi < 18.5:
        print('You are underweight. Contact your healthcare professional for further evaluation. This BMI calculator is for adults 18 years or older. So below the age of 18 is not allowed.')
    elif 18.5 <= bmi < 24.9:
        print('You are normal weight. The medical community recommends that you keep your weight within this range. This BMI calculator is for adults 18 years or older. So below the age of 18 is not allowed.')
    elif 25.0 <= bmi < 29.9:
        print('Your are over-weight. The medical community recommends talking to your healthcare professional if you have concerns about your weight. For people in this range without comorbidities, the objective is to prevent further weight gain. If you are experiencing weight-related health complications, the objective is to reduce weight. This BMI calculator is for adults 18 years or older. So below the age of 18 is not allowed.')
    elif 30.0 <= bmi < 34.9:
        print('You are in class one obesity. Having a BMI of 30 and above may mean that you have obesity and may be at risk of other weight-related complications. It is recommended that you consult your healthcare professional or another healthcare provider trained in obesity management. The goal of managing and treating obesity is not simply to lose weight, but also to improve health and lower the risks of other health complications. There are various treatment options for obesity that may be suggested for people in this category. Healthcare professionals make recommendations depending on the specific needs, current health status and whether there are any weight-related complications. Treatments can include: healthy eating, increased physical activity, behavioural therapy, obesity medications, and bariatric surgery. This BMI calculator is for adults 18 years or older. So belowthe age of 18 is not allowed.')
    elif 35.0 <= bmi < 39.9:
        print('You are in class two obesity. Having a BMI of 30 and above may mean that you have obesity and may be at risk of other weight-related complications. It is recommended that you consult your healthcare professional or another healthcare provider trained in obesity management. The goal of managing and treating obesity is not simply to lose weight, but also to improve health and lower the risks of other health complications. There are various treatment options for obesity that may be suggested for people in this category. Healthcare professionals make recommendations depending on the specific needs, current health status and whether there are any weight-related complications. Treatments can include: healthy eating, increased physical activity, behavioural therapy, obesity medications, and bariatric surgery. This BMI calculator is for adults 18 years or older. So below the age of 18 is not allowed.')
    elif 40.0 <= bmi < 49.9:
        print('You are in class three obesity. Having a BMI of 30 and above may mean that you have obesity and may be at risk of other weight-related complications. It is recommended that you consult your healthcare professional or another healthcare provider trained in obesity management. The goal of managing and treating obesity is not simply to lose weight, but also to improve health and lower the risks of other health complications. There are various treatment options for obesity that may be suggested for people in this category. Healthcare professionals make recommendations depending on the specific needs, current health status and whether there are any weight-related complications. Treatments can include: healthy eating, increased physical activity, behavioural therapy, obesity medications, and bariatric surgery. This BMI calculator is for adults 18 years or older. So below the age of 18 is not allowed.')
    elif 50.0 <= bmi < 59.9:
        print('You are in class four obesity. Having a BMI of 30 and above may mean that you have obesity and may be at risk of other weight-related complications. It is recommended that you consult your healthcare professional or another healthcare provider trained in obesity management. The goal of managing and treating obesity is not simply to lose weight, but also to improve health and lower the risks of other health complications. There are various treatment options for obesity that may be suggested for people in this category. Healthcare professionals make recommendations depending on the specific needs, current health status and whether there are any weight-related complications. Treatments can include: healthy eating, increased physical activity, behavioural therapy, obesity medications, and bariatric surgery. This BMI calculator is for adults 18 years or older. So below the age of 18 is not allowed.')
    else:
        print('You are in class five obesity. Having a BMI of 30 and above may mean that you have obesity and may be at risk of other weight-related complications. It is recommended that you consult your healthcare professional or another healthcare provider trained in obesity management. The goal of managing and treating obesity is not simply to lose weight, but also to improve health and lower the risks of other health complications. There are various treatment options for obesity that may be suggested for people in this category. Healthcare professionals make recommendations depending on the specific needs, current health status and whether there are any weight-related complications. Treatments can include: healthy eating, increased physical activity, behavioural therapy, obesity medications, and bariatric surgery. This BMI calculator is for adults 18 years or older. So below the age of 18 is not allowed.')

    print()

if __name__ == "__main__":
    main()