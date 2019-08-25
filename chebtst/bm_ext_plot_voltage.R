library(rmatio)
library(ggplot2)
library(gridExtra)

## when laml = 0.0
results0  <- read.mat('bm_ext_base_laml_0p0_Rl_1e0.mat')
vplist0   <- results0['Vplist'][[1]]
results1  <- read.mat('bm_ext_base_laml_0p0_Rl_1e1.mat')
vplist1   <- results1['Vplist'][[1]]
results2  <- read.mat('bm_ext_base_laml_0p0_Rl_1e2.mat')
vplist2   <- results2['Vplist'][[1]]
results3  <- read.mat('bm_ext_base_laml_0p0_Rl_1e3.mat')
vplist3   <- results3['Vplist'][[1]]
results4  <- read.mat('bm_ext_base_laml_0p0_Rl_1e4.mat')
vplist4   <- results4['Vplist'][[1]]
results5  <- read.mat('bm_ext_base_laml_0p0_Rl_1e5.mat')
vplist5   <- results5['Vplist'][[1]]
results6  <- read.mat('bm_ext_base_laml_0p0_Rl_1e6.mat')
vplist6   <- results6['Vplist'][[1]]
results7  <- read.mat('bm_ext_base_laml_0p0_Rl_1e7.mat')
vplist7   <- results7['Vplist'][[1]]

frlist  <- results0['frlist'][[1]]
wlist   <- 2*pi*frlist
xib   <- results0['xib']

dfs <- data.frame(frlist, vplist0, vplist1,
                  vplist2, vplist3, vplist4, 
                  vplist5, vplist6, vplist7)

p0 <- ggplot(dfs, aes(frlist, y = value, color = variable)) + 
  geom_line(aes(y = Mod(vplist0), col = "vplist0")) + 
  geom_line(aes(y = Mod(vplist1), col = "vplist1")) +
  geom_line(aes(y = Mod(vplist2), col = "vplist2")) +
  geom_line(aes(y = Mod(vplist3), col = "vplist3")) +
  geom_line(aes(y = Mod(vplist4), col = "vplist4")) +
  geom_line(aes(y = Mod(vplist5), col = "vplist5")) +
  geom_line(aes(y = Mod(vplist6), col = "vplist6")) +
  geom_line(aes(y = Mod(vplist7), col = "vplist7")) + 
  scale_y_log10() + scale_x_continuous()


## when laml = 0.1
results0  <- read.mat('bm_ext_base_laml_0p1_Rl_1e0.mat')
vplist0   <- results0['Vplist'][[1]]
results1  <- read.mat('bm_ext_base_laml_0p1_Rl_1e1.mat')
vplist1   <- results1['Vplist'][[1]]
results2  <- read.mat('bm_ext_base_laml_0p1_Rl_1e2.mat')
vplist2   <- results2['Vplist'][[1]]
results3  <- read.mat('bm_ext_base_laml_0p1_Rl_1e3.mat')
vplist3   <- results3['Vplist'][[1]]
results4  <- read.mat('bm_ext_base_laml_0p1_Rl_1e4.mat')
vplist4   <- results4['Vplist'][[1]]
results5  <- read.mat('bm_ext_base_laml_0p1_Rl_1e5.mat')
vplist5   <- results5['Vplist'][[1]]
results6  <- read.mat('bm_ext_base_laml_0p1_Rl_1e6.mat')
vplist6   <- results6['Vplist'][[1]]
results7  <- read.mat('bm_ext_base_laml_0p1_Rl_1e7.mat')
vplist7   <- results7['Vplist'][[1]]

frlist  <- results0['frlist'][[1]]
wlist   <- 2*pi*frlist
xib   <- results0['xib']

dfs <- data.frame(frlist, vplist0, vplist1,
                 vplist2, vplist3, vplist4, 
                 vplist5, vplist6, vplist7)

p1 <- ggplot(dfs, aes(frlist, y = value, color = variable)) + 
  geom_line(aes(y = Mod(vplist0), col = "vplist0")) + 
  geom_line(aes(y = Mod(vplist1), col = "vplist1")) +
  geom_line(aes(y = Mod(vplist2), col = "vplist2")) +
  geom_line(aes(y = Mod(vplist3), col = "vplist3")) +
  geom_line(aes(y = Mod(vplist4), col = "vplist4")) +
  geom_line(aes(y = Mod(vplist5), col = "vplist5")) +
  geom_line(aes(y = Mod(vplist6), col = "vplist6")) +
  geom_line(aes(y = Mod(vplist7), col = "vplist7")) + 
  scale_y_log10() + scale_x_continuous()


## when laml = 0.2
results0  <- read.mat('bm_ext_base_laml_0p2_Rl_1e0.mat')
vplist0   <- results0['Vplist'][[1]]
results1  <- read.mat('bm_ext_base_laml_0p2_Rl_1e1.mat')
vplist1   <- results1['Vplist'][[1]]
results2  <- read.mat('bm_ext_base_laml_0p2_Rl_1e2.mat')
vplist2   <- results2['Vplist'][[1]]
results3  <- read.mat('bm_ext_base_laml_0p2_Rl_1e3.mat')
vplist3   <- results3['Vplist'][[1]]
results4  <- read.mat('bm_ext_base_laml_0p2_Rl_1e4.mat')
vplist4   <- results4['Vplist'][[1]]
results5  <- read.mat('bm_ext_base_laml_0p2_Rl_1e5.mat')
vplist5   <- results5['Vplist'][[1]]
results6  <- read.mat('bm_ext_base_laml_0p2_Rl_1e6.mat')
vplist6   <- results6['Vplist'][[1]]
results7  <- read.mat('bm_ext_base_laml_0p2_Rl_1e7.mat')
vplist7   <- results7['Vplist'][[1]]

frlist  <- results0['frlist'][[1]]
wlist   <- 2*pi*frlist
xib   <- results0['xib']

dfs <- data.frame(frlist, vplist0, vplist1,
                  vplist2, vplist3, vplist4, 
                  vplist5, vplist6, vplist7)

p2 <- ggplot(dfs, aes(frlist, y = value, color = variable)) + 
  geom_line(aes(y = Mod(vplist0), col = "vplist0")) + 
  geom_line(aes(y = Mod(vplist1), col = "vplist1")) +
  geom_line(aes(y = Mod(vplist2), col = "vplist2")) +
  geom_line(aes(y = Mod(vplist3), col = "vplist3")) +
  geom_line(aes(y = Mod(vplist4), col = "vplist4")) +
  geom_line(aes(y = Mod(vplist5), col = "vplist5")) +
  geom_line(aes(y = Mod(vplist6), col = "vplist6")) +
  geom_line(aes(y = Mod(vplist7), col = "vplist7")) + 
  scale_y_log10() + scale_x_continuous()


## when laml = 0.3
results0  <- read.mat('bm_ext_base_laml_0p3_Rl_1e0.mat')
vplist0   <- results0['Vplist'][[1]]
results1  <- read.mat('bm_ext_base_laml_0p3_Rl_1e1.mat')
vplist1   <- results1['Vplist'][[1]]
results2  <- read.mat('bm_ext_base_laml_0p3_Rl_1e2.mat')
vplist2   <- results2['Vplist'][[1]]
results3  <- read.mat('bm_ext_base_laml_0p3_Rl_1e3.mat')
vplist3   <- results3['Vplist'][[1]]
results4  <- read.mat('bm_ext_base_laml_0p3_Rl_1e4.mat')
vplist4   <- results4['Vplist'][[1]]
results5  <- read.mat('bm_ext_base_laml_0p3_Rl_1e5.mat')
vplist5   <- results5['Vplist'][[1]]
results6  <- read.mat('bm_ext_base_laml_0p3_Rl_1e6.mat')
vplist6   <- results6['Vplist'][[1]]
results7  <- read.mat('bm_ext_base_laml_0p3_Rl_1e7.mat')
vplist7   <- results7['Vplist'][[1]]

frlist  <- results0['frlist'][[1]]
wlist   <- 2*pi*frlist
xib   <- results0['xib']

dfs <- data.frame(frlist, vplist0, vplist1,
                  vplist2, vplist3, vplist4, 
                  vplist5, vplist6, vplist7)

p3 <- ggplot(dfs, aes(frlist, y = value, color = variable)) + 
  geom_line(aes(y = Mod(vplist0), col = "vplist0")) + 
  geom_line(aes(y = Mod(vplist1), col = "vplist1")) +
  geom_line(aes(y = Mod(vplist2), col = "vplist2")) +
  geom_line(aes(y = Mod(vplist3), col = "vplist3")) +
  geom_line(aes(y = Mod(vplist4), col = "vplist4")) +
  geom_line(aes(y = Mod(vplist5), col = "vplist5")) +
  geom_line(aes(y = Mod(vplist6), col = "vplist6")) +
  geom_line(aes(y = Mod(vplist7), col = "vplist7")) + 
  scale_y_log10() + scale_x_continuous()



## when laml = 0.4
results0  <- read.mat('bm_ext_base_laml_0p4_Rl_1e0.mat')
vplist0   <- results0['Vplist'][[1]]
results1  <- read.mat('bm_ext_base_laml_0p4_Rl_1e1.mat')
vplist1   <- results1['Vplist'][[1]]
results2  <- read.mat('bm_ext_base_laml_0p4_Rl_1e2.mat')
vplist2   <- results2['Vplist'][[1]]
results3  <- read.mat('bm_ext_base_laml_0p4_Rl_1e3.mat')
vplist3   <- results3['Vplist'][[1]]
results4  <- read.mat('bm_ext_base_laml_0p4_Rl_1e4.mat')
vplist4   <- results4['Vplist'][[1]]
results5  <- read.mat('bm_ext_base_laml_0p4_Rl_1e5.mat')
vplist5   <- results5['Vplist'][[1]]
results6  <- read.mat('bm_ext_base_laml_0p4_Rl_1e6.mat')
vplist6   <- results6['Vplist'][[1]]
results7  <- read.mat('bm_ext_base_laml_0p4_Rl_1e7.mat')
vplist7   <- results7['Vplist'][[1]]

frlist  <- results0['frlist'][[1]]
wlist   <- 2*pi*frlist
xib   <- results0['xib']

dfs <- data.frame(frlist, vplist0, vplist1,
                  vplist2, vplist3, vplist4, 
                  vplist5, vplist6, vplist7)

p4 <- ggplot(dfs, aes(frlist, y = value, color = variable)) + 
  geom_line(aes(y = Mod(vplist0), col = "vplist0")) + 
  geom_line(aes(y = Mod(vplist1), col = "vplist1")) +
  geom_line(aes(y = Mod(vplist2), col = "vplist2")) +
  geom_line(aes(y = Mod(vplist3), col = "vplist3")) +
  geom_line(aes(y = Mod(vplist4), col = "vplist4")) +
  geom_line(aes(y = Mod(vplist5), col = "vplist5")) +
  geom_line(aes(y = Mod(vplist6), col = "vplist6")) +
  geom_line(aes(y = Mod(vplist7), col = "vplist7")) + 
  scale_y_log10() + scale_x_continuous()



## when laml = 0.5
results0  <- read.mat('bm_ext_base_laml_0p5_Rl_1e0.mat')
vplist0   <- results0['Vplist'][[1]]
results1  <- read.mat('bm_ext_base_laml_0p5_Rl_1e1.mat')
vplist1   <- results1['Vplist'][[1]]
results2  <- read.mat('bm_ext_base_laml_0p5_Rl_1e2.mat')
vplist2   <- results2['Vplist'][[1]]
results3  <- read.mat('bm_ext_base_laml_0p5_Rl_1e3.mat')
vplist3   <- results3['Vplist'][[1]]
results4  <- read.mat('bm_ext_base_laml_0p5_Rl_1e4.mat')
vplist4   <- results4['Vplist'][[1]]
results5  <- read.mat('bm_ext_base_laml_0p5_Rl_1e5.mat')
vplist5   <- results5['Vplist'][[1]]
results6  <- read.mat('bm_ext_base_laml_0p5_Rl_1e6.mat')
vplist6   <- results6['Vplist'][[1]]
results7  <- read.mat('bm_ext_base_laml_0p5_Rl_1e7.mat')
vplist7   <- results7['Vplist'][[1]]

frlist  <- results0['frlist'][[1]]
wlist   <- 2*pi*frlist
xib   <- results0['xib']

dfs <- data.frame(frlist, vplist0, vplist1,
                  vplist2, vplist3, vplist4, 
                  vplist5, vplist6, vplist7)

p5 <- ggplot(dfs, aes(frlist, y = value, color = variable)) + 
  geom_line(aes(y = Mod(vplist0), col = "vplist0")) + 
  geom_line(aes(y = Mod(vplist1), col = "vplist1")) +
  geom_line(aes(y = Mod(vplist2), col = "vplist2")) +
  geom_line(aes(y = Mod(vplist3), col = "vplist3")) +
  geom_line(aes(y = Mod(vplist4), col = "vplist4")) +
  geom_line(aes(y = Mod(vplist5), col = "vplist5")) +
  geom_line(aes(y = Mod(vplist6), col = "vplist6")) +
  geom_line(aes(y = Mod(vplist7), col = "vplist7")) + 
  scale_y_log10() + scale_x_continuous()




# grid.arrange(p1, p2, p3, p4, p5, ncol = 3)

