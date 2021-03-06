#coding = utf8
import sys
import numpy as np 
sys.path.append('./codes/')

#--------------------Read Snapshots-------------
#from dump import readdump
#inputfile = './dumpfile'
#readdump(inputfile, ndim)  #get all the informtion in dump files (one file)
#ndim declares the dimension
#x, xs, xu coordinates are accepted. 
#This part is not necesay since dump has been imported in follow modules


#--------------------Calculate Pair Correlation Functions-------------
# from paircorrelationfunctions import gr
# inputfile = '../dump/dump.CuZr.2D.lammpstrj'
# gr(inputfile, 2).getresults(outputfile = 'ZrCu.2D.dat', ppp = [1, 1], results_path = '../gr/')

# gr(inputfile, ndim).getresults(outputfile, ppp, rdelta = 0.01, results_path='../../analysis/gr/')
# gr(inputfile, ndim).Unary(outputfile, ppp, rdelta = 0.01, results_path='../../analysis/gr/')
# gr(inputfile, ndim).Binary(outputfile, ppp, rdelta = 0.01, results_path='../../analysis/gr/')
# gr(inputfile, ndim)Ternary(outputfile, ppp, rdelta = 0.01, results_path='../../analysis/gr/')
# gr(inputfile, ndim)Quarternary(outputfile, ppp, rdelta = 0.01, results_path='../../analysis/gr/')
# gr(inputfile, ndim)Quinary(outputfile, ppp, rdelta = 0.01, results_path='../../analysis/gr/')
# gr(inputfile, ndim)Senary(outputfile, ppp, rdelta = 0.01, results_path='../../analysis/gr/')
#ndim declares the dimension
#outputfile: file name of output results without path
#rdelta: bin value for gr, default = 0.01 (2D & 3D)
#ppp: set periodic boundary conditions, 1 for yes 0 for no. such as [1,1,1] (3D) and [1,1] (2D)
#results_path: set path for outcomes, default = '../../analysis/gr/' (2D & 3D)
#A numpy array of output results is returned in individual functions other than getresults()


#--------------------Calculate Structure Factors-------------
# from structurefactors import sq
# inputfile = '../dump/CuZr.xs.lammpstrj'
# sqoutputfile = 'test.binary.3D.dat'
# sq_results_path = '../Sq/'
# sq(inputfile, 3).getresults(outputfile = sqoutputfile, results_path = sq_results_path)

# sq(inputfile, ndim).getresults(outputfile, results_path = '../../analysis/sq/')
# sq(inputfile, ndim).Unary(outputfile, results_path='../../analysis/sq/')
# sq(inputfile, ndim).Binary(outputfile, results_path='../../analysis/sq/')
# sq(inputfile, ndim).Ternary(outputfile, results_path='../../analysis/sq/')
# sq(inputfile, ndim).Quarternary(outputfile, results_path='../../analysis/sq/')
# sq(inputfile, ndim).Quinary(outputfile, results_path='../../analysis/sq/')
# sq(inputfile, ndim).Senary(outputfile, results_path='../../analysis/sq/')
#outputfile: file name of output results without path
#results_path: set path for outcomes, default = '../../analysis/sq/' (2D & 3D)
#A numpy array of output results is returned in the individual functions other than getresults()

#from structurefactors import choosewavevector
#choosewavevector(Numofq, ndim) 
#function setting wave vector for structure factors
#return wave vector numpy array [d, a, b, c] d = a**2 + b**2 + c**2 (3D)
#return wave vector numpy array [d, a, b] d = a**2 + b**2 (2D)
#Numofq: the number of wavenumber considered, default = 500


# #--------------------Calculate Dynamical Properties-------------
# from dynamics import dynamics
# inputfile = '../dump/dump.CuZr.2D.lammpstrj'
# dyn_result_path = '../dynamics/'
# dynamics(inputfile, 2).total(outputfile = 'total.2D.dat', qmax = 2.50, a = 1.0, dt = 0.002, results_path = dyn_result_path)
# dynamics(inputfile, 2).partial(outputfile = 'partial.2D.dat', qmax = [2.78, 2.56], a = 1.0, dt = 0.002, results_path = dyn_result_path)
# dynamics(inputfile, 2).slowS4(outputfile = 'slowS4.2D.dat', X4time = 64, dt = 0.002, a = 1.0, results_path = dyn_result_path)
# dynamics(inputfile, 2).fastS4(outputfile = 'fastS4.2D.dat', a = 1.0, dt = 0.002, X4timeset = 64, results_path = dyn_result_path)

#get the first peaks of structure factors first for self-intermediate scattering functions
#sqvalue = np.loadtxt(sq_results_path + sqoutputfile, skiprows = 1)
#qmaxvalue = [sqvalue[sqvalue[:, i].argmax(), 0] for i in range(1, len(sqvalue[0]))]
# dynamics(inputfile, ndim).total(outputfile, qmax, a = 1.0, dt = 0.002, results_path = '../../analysis/dynamics')
# dynamics(inputfile, ndim).partial(outputfile, qmax, a = 1.0, dt = 0.002, results_path = '../../analysis/dynamics')
#qmax should be a list for partial(), such as [0, 0, 0] for ternary system. A list is returned containing results of different types in squence
#getX4value = np.loadtxt(dyn_result_path + dynoverall, skiprows = 1)
#getX4peak = getX4value[getX4value[:, 4].argmax(), 0] #just the peak time value not the interval
# dynamics(inputfile, ndim).slowS4(outputfile, X4time, dt = 0.002, a = 1.0, results_path = '../../analysis/dynamics')
# dynamics(inputfile, ndim).fastS4(outputfile, a = 1.0, dt = 0.002, X4timeset = 0, results_path = '../../analysis/dynamics')
#X4timeset can be set as in slowS4(), but can also be 0 to use the inner calculated value in fastS4(). default = 0
#outputfile: file name of output results without path
#Function total() only calculates the overall particle dynamics neglecting particle types
#Use Function partial() to calculate particle type related dynamics
#Use Function slowS4() to calculate four-point dynamic structure factor of slow atoms
#Use Function fastS4() to calculate four-point dynamic structure factor of fast atoms
#a: cutoff in the overlap function Q(t). default = 1.0
#dt: timestep in MD simulations. default = 0.002

# #--------------------Calculate Cage Relative Dynamical Properties-------------
#from cagedynamics import dynamics
# dynamics(inputfile, Neighborfile, ndim).total(outputfile, qmax, a = 1.0, dt = 0.002, results_path = '../../analysis/cagedynamics')
# dynamics(inputfile, Neighborfile, ndim).partial(outputfile, qmax, a = 1.0, dt = 0.002, results_path = '../../analysis/cagedynamics')
# dynamics(inputfile, Neighborfile, ndim).slowS4(outputfile, X4time, dt = 0.002, a = 1.0, results_path = '../../analysis/cagedynamics')
# dynamics(inputfile, Neighborfile, ndim).fastS4(outputfile, a = 1.0, dt = 0.002, X4timeset = 0, results_path = '../../analysis/cagedynamics')
#the synax of this module is the same as above of the Dynamical Properties
#but the neighbor list file should also be provided to calculate the cage relative displacements

# #--------------------Calculate BOO in 3D -------------
# from BondOOrder import BOO3D
# dumpfile = '../dump/CuZr.x.lammpstrj'
# Neighborfile = '../neighbor/amorphous/voro.CuZr.x.neighbor.dat'
# faceareafile = '../neighbor/amorphous/voro.CuZr.x.facearea.dat'
# boo = BOO3D(dumpfile, Neighborfile, faceareafile)
# filepath = '../boo/amorphous/'
# lll = 6
# boo.qlQl(lll, ppp = [1,1,1], AreaR = 0, outputql = 'sq' + str(lll) +'.dat', outputQl = 'bQ' + str(lll) +'.dat', results_path = filepath)
# boo.GllargeQ(lll, ppp = [1,1,1], rdelta = 0.01, AreaR = 0, outputgl = 'GlbQ' + str(lll) +'.dat', results_path = filepath)
# boo.smallwcap(lll, ppp = [1,1,1], AreaR = 0, outputw = 'sw' + str(lll) +'.dat', outputwcap = 'swcap' + str(lll) +'.dat', results_path = filepath)
# boo.largeWcap(lll, ppp = [1,1,1], AreaR = 0, outputW = 'bW' + str(lll) +'.dat', outputWcap = 'bWcap' + str(lll) +'.dat', results_path = filepath)
# boo.sijsmallql(l = lll, ppp = [1,1,1], AreaR = 0, c = 0.7, outputql = 'sijsq' + str(lll) +'.dat', outputsij = 'sijvaluesq' + str(lll) +'.dat', results_path = filepath)

# boo = BOO3D(dumpfile = './dump/CuZr.x.lammpstrj', Neighborfile = './neighbor/voro.CuZr.x.neighbor.dat', faceareafile = './neighbor/voro.CuZr.x.facearea.dat')
# boo.qlQl(l = lll, ppp = [1,1,1], AreaR = 0, outputql = 'sq' + str(lll) +'.dat', outputQl = 'bQ' + str(lll) +'.dat', results_path = filepath)
# boo.sijsmallql(l = lll, ppp = [1,1,1], AreaR = 0, c = 0.7, outputql = 'sijsq' + str(lll) +'.dat', outputsij = 'sijvaluesq' + str(lll) +'.dat', results_path = filepath)
# boo.sijlargeQl(l = lll, ppp = [1,1,1], AreaR = 0, c = 0.7, outputQl = 'sijbQ' + str(lll) +'.dat', outputsij = 'sijvaluebQ' + str(lll) +'.dat', results_path = filepath)
# boo.GllargeQ(l = lll, ppp = [1,1,1], rdelta = 0.01, AreaR = 0, outputgl = 'GlbQ' + str(lll) +'.dat', results_path = filepath)
# boo.Glsmallq(l = lll, ppp = [1,1,1], rdelta = 0.01, AreaR = 0, outputgl = 'Glsq' + str(lll) +'.dat', results_path = filepath)
# boo.smallwcap(l = lll, ppp = [1,1,1], AreaR = 0, outputw = 'sw' + str(lll) +'.dat', outputwcap = 'swcap' + str(lll) +'.dat', results_path = '../../analysis/BOO')
# boo.largeWcap(l = lll, ppp = [1,1,1], AreaR = 0, outputW = 'bW' + str(lll) +'.dat', outputWcap = 'bWcap' + str(lll) +'.dat', results_path = '../../analysis/BOO')
# boo.timecorr(l = lll, ppp = [1,1,1], AreaR = 0, dt = 0.002, outputfile = 'timecorr' + str(lll) +'.dat', results_path = filepath)

# boo = BOO3D(dumpfile = , Neighborfile = , faceareafile = )
# boo.qlQl(l = , ppp = [1,1,1], AreaR = 0, outputql = '', outputQl = '', results_path = '../../analysis/BOO')
# #Give names to outputql and outputQl to store the data or no data will be dumped
# #Both results will be returned in a tuple (ql, Ql)
# boo.sijsmallql(l = , ppp = [1,1,1], AreaR = 0, c = 0.7, outputql = '', outputsij = '', results_path = '../../analysis/BOO')
# boo.sijlargeQl(l = , ppp = [1,1,1], AreaR = 0, c = 0.7, outputQl = '', outputsij = '', results_path = '../../analysis/BOO')
# #c is a cutoff demonstrating whether a bond is crystalline or not
# #Give names to outputql and outputsij to store the results
# #only individual sij results will be returned as a numpy array
# boo.GllargeQ(l = , ppp = [1,1,1], rdelta = 0.01, AreaR = 0, outputgl = 'GllargeQ.dat', results_path = '../../analysis/BOO')
# boo.Glsmallq(l = , ppp = [1,1,1], rdelta = 0.01, AreaR = 0, outputgl = 'Glsmallq.dat', results_path = '../../analysis/BOO')
# #rdelta is the bin size in calculating g(r) and Gl(r)
# #results of g(r) and Gl(r) are returned as a numpy array
# boo.smallwcap(l, ppp = [1,1,1], AreaR = 0, outputw = '', outputwcap = '', results_path = '../../analysis/BOO')
# boo.largeWcap(l, ppp = [1,1,1], AreaR = 0, outputW = '', outputWcap = '', results_path = '../../analysis/BOO')
#Give names to outputw, outputW, outputwcap, outputWcap to store the data, default is none
#results of w and W including normalized ones are returned in a tuple (w, w_cap) or (W, W_cap)
# boo.timecorr(l, ppp = [1,1,1], AreaR = 0, dt = 0.002, outputfile = 'timecorr.dat', results_path = '../../analysis/BOO'):
#AreaR = 0 indicates calculate traditional ql and Ql.  default = 0
#AreaR = 1 indicates calculate voronoi polyhedron face area weighted ql and Ql
#ppp: set periodic boundary conditions, 1 for yes 0 for no. default = [1,1,1] (3D)

# --------------------Rewrite Neighbor list from LAMMPS Voronoi -------------
# from ParseList import readall
# for j in ['sc', 'bcc', 'fcc', 'hcp']:
#     fnfile = './neighbor/' + j + '.neighborlist.dat'
#     fffile = './neighbor/' + j + '.facearealist.dat'
#     fread  = './dump/dump.' + j + '.neighbors.dat'
#     if j is 'sc': ParticleNumber = 1000
#     if j is 'bcc': ParticleNumber = 2000
#     if j is 'fcc': ParticleNumber = 4000
#     if j is 'hcp': ParticleNumber = 4000
#     readall(fnfile, fffile, fread, ParticleNumber, Snapshotnumber = 2)
# readall(fnfile, fffile, fread, ParticleNumber, Snapshotnumber)
#The files are neighborfile, faceareafile, readindumpfile in order


#--------------------Calculate Binder cumulant -------------
# from Binder import BCumulant
# BCumulant('../dump/CuZr.x.lammpstrj', 3).BCall(outputfile = 'binderCuZr.dat', results_path = '../dynamics/')

# BCumulant(inputfile, ndim).BCall(outputfile, a = 1.0, dt = 0.002, results_path = '../../analysis/dynamics')
# BCumulant(inputfile, ndim).BCtype(outputfile, a = 1.0, dt = 0.002, results_path = '../../analysis/dynamics')
#outputfile is the file name of outputs 
#a is the cutoff in the overlap function of Binder, default = 1.0
#dt is the time step of MD simulation, default = 0.002
#results_path is the file path of the outputs, default = '../../analysis/dynamics'


#--------------------Calculate Bond Orietational Order at 2D -------------
# from Order2D import BOO2D
# dumpfile = '../dump/dump.CuZr.2D.lammpstrj'
# Neighborfile = '../Order2D/neighborlist-gr-0K-1.dat'
# BOO2D(dumpfile, Neighborfile).tavephi(outputphi = 'phi6.dat', outputavephi = 'ave_phi6.dat', l = 6, ppp = [1, 1], avet = 64, dt = 0.002, results_path = '../Order2D/')
# BOO2D(dumpfile, Neighborfile).spatialcorr(outputfile = 'g6.dat', l = 6, ppp = [1, 1], rdelta = 0.01, results_path = '../Order2D/')
# BOO2D(dumpfile, Neighborfile).timecorr(outputfile = 'time6.dat', l = 6, ppp = [1, 1], dt = 0.002, results_path = '../Order2D/')

# BOO2D(dumpfile, Neighborfile).tavephi(outputphi, outputavephi, avet, l = 6, ppp = [1, 1], dt = 0.002, results_path = '../../analysis/order2d/')
# BOO2D(dumpfile, Neighborfile).spatialcorr(outputfile, l = 6, ppp = [1, 1], rdelta = 0.01, results_path = '../../analysis/order2d/')
# BOO2D(dumpfile, Neighborfile).timecorr(outputfile, l = 6, ppp = [1, 1], dt = 0.002, results_path = '../../analysis/order2d/')
#outputphi and outputavephi are the filenames of absolute phi and time-averaged phi. Give them names to calculate and write them to files
#l is the degree of BOO, from 4 - 8 normally in 2D
#ppp is the periodic boundary conditions, set 1 for yes and 0 for no, default = [1, 1]
#dt is the timestep of simulation, default = 0.002
#results_path is the file path of the outputs, default = '../../analysis/order2d/'
