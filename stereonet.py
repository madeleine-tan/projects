# Create equal-area lower-hemisphere stereonet and density contour stereonet
# Uses mplstereonet by Joe Kington: https://pypi.org/project/mplstereonet/

import numpy as np
import mplstereonet
import matplotlib.pyplot as plt
from collections import OrderedDict
import pandas as pd

data = pd.read_csv('./stereonet.txt', header=None, sep=None)
df = np.array(data)
strikes = np.array(df[:,0])
dips = np.array(df[:,1])

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='stereonet')
ax.grid()
ax.set_title('Stereonet', y=1.10, fontsize=15)
ax.plane(strikes, dips, c='k')
ax.pole(strikes, dips, c='k')
ax.set_azimuth_ticks([])

#finding axial plane and pole
#strike, dip = mplstereonet.fit_girdle(strikes, dips) #find axial plane
#ax.pole(strike, dip, c='r') #find pole of axial plane
#ax.plane(strike, dip, c='r', label='axial plane') #find axial plane

#finding density contour
#ax.density_contourf(strikes, dips, measurement='poles', cmap='Reds')
#ax.set_title('Density contour of the Poles', y=1.10, fontsize=15)

#creating degree labels
label = np.arange(0,360,45)
labx= 0.5-0.55*np.cos(np.radians(label+90))
laby= 0.5+0.55*np.sin(np.radians(label+90))
for i in range(len(label)):
    ax.text(labx[i],laby[i],str(int(label[i]))+'\N{DEGREE SIGN}', transform=ax.transAxes, ha='center', va='center')
    
#ax.legend(loc=4)
plt.savefig('stereonet3.pdf')
plt.show()
