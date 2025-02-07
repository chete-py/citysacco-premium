import streamlit as st
import pandas as pd

view1, view2 = st.tabs(["Premium", "Scope Of Cover"])

with view1:

    reg = st.text_input('Enter Registration')            
    value = int(st.number_input('Sum Insured')) 
    loss_of_use = st.selectbox("Choose Loss Of Use Amount charged", ["Inclusive", "Excluded"])
    span = st.selectbox("Choose Length of cover", ["Annual Cover", "Pro-Rated Cover"])
    if span == "Pro-Rated Cover":                
        days = st.number_input('Number of days on cover')   
    else:
        days = 365           
    
    if value < 2500000:
        cannon_rate = 4.5
        cannon_premium = max(value * (cannon_rate/100) * (days/365),(35000 * (days/365)))
    elif 2499999 < value < 5000000:
        cannon_rate = 4
        cannon_premium = max(value * (cannon_rate/100) * (days/365),(35000 * (days/365)))
    elif value > 4999999:
        cannon_rate = 3
        cannon_premium = (value * (cannon_rate/100) * (days/365))

    if value < 500000:
        apa_rate = 'TPO'
        apa_premium = 0
        apa_total = 'NA'
    else:
        if 500000 < value < 2500000:
            apa_rate = 4
            apa_premium = max(value * (apa_rate/100) * (days/365),(42500 * (days/365)))
        elif 2499999 < value < 5000000:
            apa_rate = 3.5
            apa_premium= max(value * (apa_rate/100) * (days/365), (42500 * (days/365)))
        elif value > 4999999:
            apa_rate = 3
            apa_premium= (value * (apa_rate/100) * (days/365))  
    
    
    # if value > 0:
    #     apa_rate = 3.5
    #     apa_premium = max(value * (apa_rate/100) * (days/365), (25000 * (days/365)))
   
    if value < 1000000:
        icea_rate = 5.35      
        icea_premium = max(value * (icea_rate/100) * (days/365),(30000 * (days/365)))                      
    elif 999999 < value < 2500000:
        icea_rate = 4.25 
        icea_premium = (value * (icea_rate/100) * (days/365))
    elif value > 2499999:
        icea_rate = 3.5 
        icea_premium = (value * (icea_rate/100) * (days/365))

        
    car_hire = 0
    car_hire_nil = 0    
    car_hire_two = 0
    fee = 100
    ex_pr = 0
    pvt_value = 0

    if st.button("Calculate"):

        if loss_of_use == 'Exluded':
            car_hire += 0
            car_hire_two += 0
        elif loss_of_use == 'Inclusive':
            car_hire_nil += 0
            car_hire_two += 3000       
                        
        cannon_gross_premium = (cannon_premium + car_hire_two)
        icea_gross_premium = (icea_premium + car_hire_two)        
        apa_gross_premium = ( apa_premium + car_hire_two)
        
        cannon_levies = cannon_gross_premium * 0.0045
        icea_levies = icea_gross_premium * 0.0045
        apa_levies = apa_gross_premium * 0.0045
               

        cannon_total = ( cannon_gross_premium + fee + cannon_levies )
        icea_total = ( icea_gross_premium + fee + icea_levies )        
        apa_total = ( apa_gross_premium + fee + apa_levies )
        

        # Format numbers with commas for thousands
        def format_with_commas(number):
            rounded_number = round(number, 2)
            return "{:,.2f}".format(rounded_number)
            
        
        formatted_value = format_with_commas(value)

        

        formatted_cannon_premium = format_with_commas(cannon_premium)        
        formatted_icea_premium = format_with_commas(icea_premium)
        formatted_apa_premium = format_with_commas(apa_premium)
        
        
        formatted_car_hire = format_with_commas(car_hire)
        formatted_car_hire_nil = format_with_commas(car_hire_nil)
        formatted_car_hire_two = format_with_commas(car_hire_two)

        
        
        formatted_icea_gross_premium = format_with_commas(icea_gross_premium)
        formatted_apa_gross_premium = format_with_commas(apa_gross_premium)
        formatted_cannon_gross_premium = format_with_commas(cannon_gross_premium)
       

        formatted_icea_levies = format_with_commas(icea_levies)
        formatted_apa_levies = format_with_commas(apa_levies)
        formatted_cannon_levies = format_with_commas(cannon_levies)

        
        formatted_icea_total = format_with_commas(icea_total)
        formatted_apa_total = format_with_commas(apa_total)              
        formatted_cannon_total = format_with_commas(cannon_total)
       
        # Create an HTML report
        html_report = f"""
        <html>
        <head>
        <style>                
            table {{
            border-collapse: collapse;
            width: 45%;
            margin: 0.5px auto; /* Center the table */
            table-layout: fixed;
            font-size: 8px;
            font-family: Candara;
        }}

        th, td {{
            border: 1px solid black;
            padding: 2.5px; /* Increased padding for better spacing */
            text-align: left;
        }}

        th {{
            background-color: #ffffff;
            color: black; /* Text color for table headers */
        }}

        .bold {{
            font-weight: bold;
        }}

        .gross_premium {{
            border-top: 2px solid black;
            border-bottom: 2px double black;        
        }}

        .footer-row th {{
            background-color: #073980;
        }}

        img {{
            width: 100%;
            height: 45px; 
            display: block;
            margin: 0 auto;
            object-fit: cover;
        }}     
        
        </style>
        </head>
        <body>
        <table>
            <tr>
                <th colspan="8" style="background-color: #966fd6; text-align: center; font-size: 12px;">INSURANCE BROKER: GRAS SAVOYE KENYA</th>
            </tr>

            <tr>
                <th colspan="2">MOTOR PRIVATE COMPREHENSIVE</th>
                <th colspan="2"><img src="https://th.bing.com/th/id/OIP.FKycthqs_eBeEyXkHC5blAHaHa?rs=1&pid=ImgDetMain" alt="Cannon Logo"></th>                       
                <th colspan="2"><img src="https://sokodirectory.com/wp-content/uploads/2015/04/APA-Insurance1.jpg" alt="APA Logo"></th>
                <th colspan="2"><img src="https://th.bing.com/th/id/OIP.uxjOhVxnL1cs8CrOBZqzjwAAAA?pid=ImgDet&w=195&h=129&c=7&dpr=1.5" alt="icea Logo"></th>
                
                </tr>
            
                <tr>
                <th style="background-color: #17B169">{reg}</th>
                <th style="background-color: #17B169">Value - KES</th>
                <th style="background-color: #17B169">Rate</th>
                <th style="background-color: #17B169">Premium</th>
                <th style="background-color: #17B169">Rate</th>
                <th style="background-color: #17B169">Premium</th>
                <th style="background-color: #17B169">Rate</th>
                <th style="background-color: #17B169">Premium</th>
               
                                                                
            <tr>
                <td>Basic Premium</td>
                <td>{value}</td> 
                <td style="color:red">{cannon_rate}%</td>
                <td>{formatted_cannon_premium}</td>
                <td style="color:red">{apa_rate}%</td>
                <td>{formatted_apa_premium}</td> 
                <td style="color:red">{icea_rate}%</td>
                <td>{formatted_icea_premium}</td> 
               
            </tr>                     

            <tr>
                <td>Excess Protector - (Material Damage)</td>
                <td></td>
                <td style="color:red">Inclusive</td>
                <td >0.00</td>                       
                <td style="color:red">Inclusive</td>  
                <td >0.00</td>
                <td style="color:red">Inclusive</td>
                <td >0.00</td>              
                
                                            
            </tr>           
                                        
            <tr>
                <td>Political/Terrorism</td>
                <td></td>
                <td style="color:red">Inclusive</td>
                <td >0.00</td>                       
                <td style="color:red">Inclusive</td>  
                <td >0.00</td>
                <td style="color:red">Inclusive</td>
                <td >0.00</td>            
                                                        
            </tr>              

            <tr>
                <td>Courtesy Car</td>                        
                <td></td>
                <td style="color:red" >3000</td>
                <td>{formatted_car_hire_two}</td>
                <td style="color:red" >3000</td>
                <td>{formatted_car_hire_two}</td>
                <td style="color:red" >3000</td>
                <td>{formatted_car_hire_two}</td>
               
                
            </tr>      
                
            
            <tr>
                <td>Gross Premium</td>
                <td></td> 
                <td></td>
                <td class='gross_premium'>{formatted_cannon_gross_premium}</td> 
                <td></td>
                <td class='gross_premium'>{formatted_apa_gross_premium}</td> 
                <td></td>
                <td class='gross_premium'>{formatted_icea_gross_premium}</td> 
                              
            </tr>      
        
            <tr>
                <td>Levies</td>
                <td></td>
                <td style="color:red">0.45%</td>
                <td >{formatted_cannon_levies}</td> <!-- Updated formatting for better readability -->
                <td style="color:red">0.45%</td>
                <td >{formatted_apa_levies}</td> <!-- Updated formatting for better readability -->
                <td style="color:red">0.45%</td>
                <td >{formatted_icea_levies}</td> <!-- Updated formatting for better readability -->             
                
        
            <\tr>
            
            <tr>
                <td>Policy Fee</td>
                <td></td>
                <td></td>
                <td>{fee}</td>
                <td></td>
                <td>{fee}</td>
                <td></td>
                <td>{fee}</td>
                               
                                                    
            </tr>
            
            <tr style=" border-top: 2px double black;  border-bottom: 2px double black;">
                <td class= 'bold' style="color:#152637">Total Premium</td>
                <td></td>
                <td></td>
                <td class = 'bold' style="color:#152637">{formatted_cannon_total}</td>
                <td></td>
                <td class = 'bold' style="color:#152637">{formatted_apa_total}</td>
                <td></td>
                <td class = 'bold' style="color:#152637">{formatted_icea_total}</td>                                                                
            </tr>                   
            <tr>
                <th colspan="8" style="color: white; background-color: #002395; text-align: center; font-size: 12px;">Additional 10% to be charged on windscreen value above 50,000 (free limit) <br> For assistance call: Chete - 0791530369</th>
            </tr>
        </table>
        </body>                    
        </html>"""

        
    # Create a download button with customized file name

        st.download_button(
            label=f"Download {reg}'s_premium_quote(HTML)",
            data=html_report.encode('utf-8'),
            file_name=f"{reg}_quote.html",
            mime="text/html"
        )
