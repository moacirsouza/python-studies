day = int(input("Day? > "))

phases = {1:"New Moon", 2:"New Moon", 3:"Wax Quarter", 4:"Wax Quarter", 
          5:"Wax Half", 6:"Wax Half", 7:"Wax Gibbons", 8:"Wax Gibbons",
          9:"Full Moon", 10:"Full Moon", 11:"Wan Gibbons", 12:"Wan Gibbons",
          13:"Wan Half", 14:"Wan Half", 15:"Wan Quarter", 16:"Wan Quarter"}

remainder = day%16

# The remainder values go from 0 to 15, but there's no day "0" in the game, so,
# whenever a day number divisible by 16 shows up, I just force the remainder to
# be 16 and index it to the "Wan Quarter" phase
if remainder ==  0:
    remainder = 16

print(f'The moon phase will be "{phases[remainder]}"')
