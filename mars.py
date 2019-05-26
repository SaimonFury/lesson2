import ephem

mars = ephem.mars('2000/01/01')
const = ephem.constellation(mars)

print(const)