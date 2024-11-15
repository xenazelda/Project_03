import calendar

# availability options: preferred, available (default), unavailable
# class to define the caregiver
class CareGiver:
    def __init__(self, name, phone, email, pay_rate = 20):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate # caregivers are paid $20/hr
        self.hours = 0 # initial 0 hours

    # sets the availability based on the shift preference
   # def set_availability(self, shift, shift_preference):
   #     if shift in self.availability:
    #        self.availability[shift] = shift_preference
    
    # adds the hours worked
    def hours_worked(self, hours):
        self.hours += hours

    # calculates weekly pay based on the assigned hours (only for paid caregivers)
    def calculate_weekly_pay(self):
        gross = self.hours * self.pay_rate
        return gross
    
# class to set up the schedule for the caregivers
# example was given (?)
class Schedule:
    def __init__(self):
        self.schedule = {} 
        self.caregivers = [] # list of caregivers
        self.availability_options = ['Preferred', 'Available', 'Unavailable']

    # default availability schedule where all shifts = "available"
    def default_schedule(self):
        for day in range(1, 8):
            self.schedule[day] = {'7:00 AM - 1:00 PM' : 'Available', 
                                  '1:00 PM - 7:00 PM' : 'Available'}

   # update schedule based on the availability preferences
    def update_schedule(self):
        day_names = list(calendar.day_name)  # ['Monday', 'Tuesday', ...]
    
        for day in range(1, 8):
            print(f"\nAvailability for {day_names[day - 1]}")
        
        # Get availability for the morning shift
        morning_shift = input("Morning shift (7:00AM - 1:00PM): Enter 'preferred', 'available', or 'NA' (default is 'available'): ").strip().lower()
        if morning_shift in self.availability_options:
            self.schedule[day]["7:00AM - 1:00PM"] = morning_shift
        
        # Get availability for the afternoon shift
        afternoon_shift = input("Afternoon shift (1:00PM - 7:00PM): Enter 'preferred', 'available', or 'NA' (default is 'available'): ").strip().lower()
        if afternoon_shift in self.availability_options:
           self.schedule[day]["1:00PM - 7:00PM"] = afternoon_shift

    # displays the updated schedule
    def display_schedule(self):
        pass