

start_time    = input ('start time (HH:MM)')
start_hours   =   int ( start_time [0:2] )
start_minutes =   int ( start_time [3:5] )

end_time    =  input ('end time (HH:MM)')
end_hours   =  int   (end_time [0:2])
end_minutes =  int   (end_time [3:5])

duration_h = end_hours   - start_hours
duration_m = end_minutes - start_minutes

duration_m_total = duration_h * 60 + duration_m + 24 * 60 * ( start_hours > end_hours )

duration_h_f = duration_m_total // 60
duration_m_f = duration_m_total - duration_h_f * 60 


print('Event duration:' , duration_h_f , 'H' , duration_m_f , 'm' )
