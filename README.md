# WNLab-2
## Observation 
### Estimate the length of a delimiter
1. A delimiter spans about 90 pixels
2. A `H` or `L` in a delimiter spans about 6 pixels

### Position of double *Da*s
- The 14th frame of `0.mp4` contains double *Da*s
- The 25th frame of `14.mp4` contains double *Da*s

### Property of autocorrelation
If there is a local minimum, then it should be one of the followings:
- delimiter Da
- delimiter Db
- delimiter Fa
- delimiter Fb
- bit 0
- bit 1

## TODO
- [ ] Find the positions of local minimal autocorrelations in a frame
- [ ] Determine whether there are Da, Db, Fa, Fb, bit 0, or bit 1  (Maybe use inner product?), and get a sequence for every frame
- [ ] Use the sequence in every frame to infer the final bit message
