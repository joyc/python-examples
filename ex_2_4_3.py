easy_pace_seconds = 8 * 60 + 15
tempo_seconds = 7 * 60 + 12
miles_at_easy_pace = 1 + 1
miles_at_tempo = 3
total_seconds = (miles_at_easy_pace * easy_pace_seconds) + (miles_at_tempo * tempo_seconds)

print "Total running time:", total_seconds, "seconds"

# division for minutes_ran is integer division, so it drops the fractions
minutes_ran = total_seconds / 60
seconds_ran = total_seconds - (minutes_ran * 60)

print "Running time in minutes:", (minutes_ran + seconds_ran/60.0)

start_time_hours = 6
start_time_minutes = 52
start_minutes_after_midnight = start_time_hours * 60 + start_time_minutes

end_minutes_after_midnight = start_minutes_after_midnight + minutes_ran

end_time_hours = end_minutes_after_midnight / 60
end_time_minutes = end_minutes_after_midnight - (end_time_hours * 60)

end_time_str = str(end_time_hours) + ":" + str(end_time_minutes) + ":" + str(seconds_ran)
print end_time_str
