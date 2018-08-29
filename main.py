import generation_mix
import pie_chart
import pprint


pp = pprint.PrettyPrinter(indent=4)

# Test getting data from gen mix and pass to pie chart
gen_mix_last_30_mins = generation_mix.get_last_30_mins("dirty")
gen_mix_pie_chart = pie_chart.calc_parts(gen_mix_last_30_mins, "cumulative")

pp.pprint(gen_mix_pie_chart)
