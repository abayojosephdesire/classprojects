def part_b(annual_salary, percent_saved, total_cost_of_home, semi_annual_raise):
	#########################################################################
	
	percent_down_payment=0.12
	amount_saved=0
	r=0.06
	months=0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ##
	###############################################################################################
	
	# Check if the amount_saved is still below the required down payment
	while amount_saved < total_cost_of_home * percent_down_payment:
	
	    # Formula: amount_saved*r/12 equals the interest added every month
	    # Formula: annual_salary*percent/12 is the percentage of the monthly salary that is saved
	    amount_saved += amount_saved*r/12 + annual_salary*percent_saved/12
	    months+=1
	
	    # Check if months is divisible by 6 and add semi_annual_raise
	    if months%6 == 0:
	        annual_salary += annual_salary*semi_annual_raise
	
	print("Number of months:", months)
	return months