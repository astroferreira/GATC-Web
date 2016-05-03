from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from discoverGalaxy.models import Galaxy
import os 
import numpy as np
import matplotlib.pyplot as plt
import pyfits
import matplotlib as mpl


"""
files = sorted(os.listdir('/data/mysample/original/ima_g/'))


rootname50,Mo,No,psffwhm,asecpix,skybg,skybgstd,x0peak,y0peak,x0col,y0col,x0A1fit,y0A1fit,x0A3fit,y0A3fit,a,b,PAdeg,InFit1D,RnFit1D,nFit1D,xsin,x0Fit2D,y0Fit2D,InFit2D,RnFit2D,nFit2D,qFit2D,PAFit2D,Rp,C1,C2,R20,R50,R80,R90,A1,A2,A3,A4,S1,S3,G,M20,psi,sigma_psi,H,QF,error  = np.loadtxt('/data/data.MFMTK', dtype=str, delimiter=',').T
galaxiesNames  = np.loadtxt('/data/mysample/mydata/resolution/edit_data_1024_g.mfmtk', dtype=str, delimiter=',').T
pathImg = "img/output/site/"
pathMfmtk = "img/output/mfmtk_png/"

pathResolutionMFMTK = "img/output/samplingStudy/"

labels = ['redshift','Mo','No','psffwhm','asecpix','skybg','skybgstd','x0peak','y0peak','x0col','y0col','x0A1fit','y0A1fit','x0A3fit','y0A3fit ','a','b','PAdeg','InFit1D','RnFit1D','nFit1D','xsin','x0Fit2D','y0Fit2D','InFit2D','RnFit2D','nFit2D256','qFit2D','PAFit2D','RpO','C1256','C2256','R20','R50','R80','R90','A1256','A2256','A3256','A4256','S1256','S3256','G256','M20','psi','sigma_psi','H','QF','erro']

font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 20,
        }

font2 = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 5,
        }

files = sorted(os.listdir('/data/output/img/original/ima_g/'))

rootname50,Mo,No,psffwhm,asecpix,skybg,skybgstd,x0peak,y0peak,x0col,y0col,x0A1fit,y0A1fit,x0A3fit,y0A3fit,a,b,PAdeg,InFit1D,RnFit1D,nFit1D,xsin,x0Fit2D,y0Fit2D,InFit2D,RnFit2D,nFit2D,qFit2D,PAFit2D,Rp,C1,C2,R20,R50,R80,R90,A1,A2,A3,A4,S1,S3,G,M20,psi,sigma_psi,H,QF,error  = np.loadtxt('/data/data.MFMTK', dtype=str, delimiter=',').T

pathImg = "img/output/original/site/color/"
pathMfmtk = "img/output/mfmtk_img/"

"""
def index(request):
	template = loader.get_template('discoverGalaxy/index.html')
	
	arquivos = np.loadtxt('/data/output/site/galaxylist', dtype=str)[0:100]
	"""
	
	names = np.loadtxt('/data/output/site/galaxylist', dtype=str)
	for f in names:
		galaxyName = f
		galaxyId = galaxyName.split('PGC')[1]
		colorUrl = pathImg + 'color/' + galaxyName + '.png'
	"""
	galaxies = []
	#arquivos = files[0:100]
	pathImg = "img/output/site/color/"
	for f in arquivos:
		galaxyName = f.split('.')[0]
		galaxyId = galaxyName.split('PGC')[1]
		colorUrl = pathImg  + galaxyName + '.png'
		Gal = Galaxy(galId=galaxyId, name=galaxyName, colorImgUrl=colorUrl)
		galaxies.append(Gal)
	
	context = RequestContext(request, {
		'galaxyList': galaxies
		})
	return HttpResponse(template.render(context))

#def home(request):


def sampleStats(request):
	template = loader.get_template('discoverGalaxy/sample.html')
	context = RequestContext(request, {
		'sample_histogram': 'img/output/site/sample.png'
		})
	return HttpResponse(template.render(context))



"""
def detail(request, pgc_id):
	galaxyName = "PGC" + str(pgc_id)
	index = np.where(rootname50 == (galaxyName + "_g"))
	gal = rootname50[index][0]
	colorUrl = pathImg + 'color/' + galaxyName + '.png'
	galaxy = Galaxy(galId=pgc_id, name=galaxyName, colorImgUrl=colorUrl)
	#for f in files:
	#	f.split('_')[0]
	template = loader.get_template('discoverGalaxy/detail.html')
	imggif = None
	redshiftImages = None
	if (galaxyName == "PGC0000282"):
		imggif = 'img/output/thisismygif.gif'
		redshiftImages = sorted(os.listdir('/data/output/examination/282/512/img/'))

	redshiftPath = 'img/output/examination/282/512/img/'
	A1_img = None
	A3_img = None
	C1_img = None
	C2_img = None
	S1_img = None
	S3_img = None
	G_img = None
	M20_img = None
	n_img = None
	#Generate if not A1

	if os.path.isfile('/data/output/datalogs/' + galaxyName + '.mfmtk'):
		mpc, Mo,No,psffwhm,asecpix,skybg,skybgstd,x0peak,y0peak,x0col,y0col,x0A1fit,y0A1fit,x0A3fit,y0A3fit,a, b, PAdeg, In, Rn, n,xsin,x0Fit2D,y0Fit2D, InFit2D,RnFit2D,nFit2D,qFit2D,PAFit2D,Rp, C1, C2, R20,R50,R80,R90, A1, A2, A3, A4, S1,S3,G,M20,psi,sigma_psi,H,QF,error = np.genfromtxt('/data/output/datalogs/' + galaxyName + '.mfmtk', delimiter=',').T  
		if not os.path.isfile('/data/output/datalogs/A1/' + galaxyName + '.png'):
			fig = plt.figure(1)
			plt.plot(mpc, A1, '-', color='black')
			A1_img = 'img/output/datalogs/A1/' + galaxyName + '.png'
			plt.xlabel(r'$\rm Distance \ [Mpc]$', fontdict=font)
			plt.ylabel(r'$\rm Asymmetry \ 1$', fontdict=font)
			fig.savefig('/data/output/datalogs/A1/' + galaxyName + '.png', format='png')
			fig.clf()
		else:
			A1_img = 'img/output/datalogs/A1/' + galaxyName + '.png'
		if not os.path.isfile('/data/output/datalogs/A3/' + galaxyName + '.png'):
			fig = plt.figure(1)
			plt.plot(mpc, (1-A3), '-', color='black')
			A3_img = 'img/output/datalogs/A3/' + galaxyName + '.png'
			plt.xlabel(r'$\rm Distance \ [Mpc]$', fontdict=font)
			plt.ylabel(r'$\rm Asymmetry \ 3$', fontdict=font)
			fig.savefig('/data/output/datalogs/A3/' + galaxyName + '.png', format='png')
			fig.clf()
		else:
			A3_img = 'img/output/datalogs/A3/' + galaxyName + '.png'
		if not os.path.isfile('/data/output/datalogs/C1/' + galaxyName + '.png'):
			fig = plt.figure(1)
			plt.plot(mpc, C1, '-', color='black')
			C1_img = 'img/output/datalogs/C1/' + galaxyName + '.png'
			plt.xlabel(r'$\rm Distance \ [Mpc]$', fontdict=font)
			plt.ylabel(r'$\rm Concentration \ 1$', fontdict=font)
			fig.savefig('/data/output/datalogs/C1/' + galaxyName + '.png', format='png')
			fig.clf()
		else:
			C1_img = 'img/output/datalogs/C1/' + galaxyName + '.png'
		if not os.path.isfile('/data/output/datalogs/C2/' + galaxyName + '.png'):
			fig = plt.figure(1)
			plt.plot(mpc, C2, '-', color='black')
			C2_img = 'img/output/datalogs/C2/' + galaxyName + '.png'
			plt.xlabel(r'$\rm Distance \ [Mpc]$', fontdict=font)
			plt.ylabel(r'$\rm Concentration \ 2$', fontdict=font)
			fig.savefig('/data/output/datalogs/C2/' + galaxyName + '.png', format='png')
			fig.clf()
		else:
			C2_img = 'img/output/datalogs/C2/' + galaxyName + '.png'
		if not os.path.isfile('/data/output/datalogs/S1/' + galaxyName + '.png'):
			fig = plt.figure(1)
			plt.plot(mpc, S1, '-', color='black')
			S1_img = 'img/output/datalogs/A3/' + galaxyName + '.png'
			plt.xlabel(r'$\rm Distance \ [Mpc]$', fontdict=font)
			plt.ylabel(r'$\rm Smoothness \ 1$', fontdict=font)
			fig.savefig('/data/output/datalogs/S1/' + galaxyName + '.png', format='png')
			fig.clf()
		else:
			S1_img = 'img/output/datalogs/S1/' + galaxyName + '.png'
		if not os.path.isfile('/data/output/datalogs/S2/' + galaxyName + '.png'):
			fig = plt.figure(1)
			plt.plot(mpc, S3, '-', color='black')
			S3_img = 'img/output/datalogs/S2/' + galaxyName + '.png'
			plt.xlabel(r'$\rm Distance \ [Mpc]$', fontdict=font)
			plt.ylabel(r'$\rm Smoothness \ 3$', fontdict=font)
			fig.savefig('/data/output/datalogs/S2/' + galaxyName + '.png', format='png')
			fig.clf()
		else:
			S3_img = 'img/output/datalogs/S2/' + galaxyName + '.png'







	#
	# Morfometryka output images for each sampling step
	#
	mfmtk_pngs = [pathResolutionMFMTK + '256/mfmtk_png/g/' + galaxyName + '_g_mfmtk.png',pathResolutionMFMTK + '384/mfmtk_png/g/' + galaxyName + '_g_mfmtk.png',pathResolutionMFMTK + '512/mfmtk_png/g/' + galaxyName + '_g_mfmtk.png',pathResolutionMFMTK + '768/mfmtk_png/g/' + galaxyName + '_g_mfmtk.png', pathResolutionMFMTK + '1024/mfmtk_png/g/' + galaxyName + '_g_mfmtk.png']

	#
	# Graphs for the effect of sampling in individual galaxies
	#
	# load everything
	resolutionImages = []
	resolutionImages.append('img/output/samplingStudy/graphs/parameters/' + galaxyName + '.png')
	
	context = RequestContext(request, {
		'galaxy': galaxy,
		'u_img': pathImg + 'u/' + galaxyName + '_u.png',
		'g_img': pathImg + 'g/' + galaxyName + '_g.png',
		'r_img': pathImg + 'r/' + galaxyName + '_r.png',
		'i_img': pathImg + 'i/' + galaxyName + '_i.png',
		'z_img': pathImg + 'z/' + galaxyName + '_z.png',
		'gal': gal,		
		'mfmtk_out' : pathMfmtk + galaxyName + '_g_mfmtk.png',
		'imggif' : imggif,
		'A1_img': A1_img,
		'A3_img': A3_img,
		'C1_img': C1_img,
		'C2_img': C2_img,
		'S1_img': S1_img,
		'S3_img': S3_img,
		'redshiftPath': redshiftPath,
		'redshiftImages': redshiftImages,
		'mfmtk_pngs' : mfmtk_pngs,
		'resolutionImages' : resolutionImages

	#for f in files:
	#	f.split('_')[0]
	template = loader.get_template('discoverGalaxy/detail.html')
	context = RequestContext(request, {
		'galaxyName': galaxyName,
		'galaxyId': pgc_id,
		'u_img': pathImg + 'ima_u/' + galaxyName + '.png',
		'g_img': pathImg + 'ima_g/' + galaxyName + '.png',
		'r_img': pathImg + 'ima_r/' + galaxyName + '.png',
		'i_img': pathImg + 'ima_i/' + galaxyName + '.png',
		'z_img': pathImg + 'ima_z/' + galaxyName + '.png',
		'gal': gal,		
		'Mo' : Mo[index][0],
		'No' : No[index][0],
		'psffwhm' : psffwhm[index][0],
		'asecpix' : asecpix[index][0],
		'skybg' : skybg[index][0],
		'skybgstd' : skybgstd[index][0],
		'x0peak' : x0peak[index][0],
		'y0peak' : y0peak[index][0],
		'x0col' : x0col[index][0],
		'y0col' : y0col[index][0],
		'x0A1fit' : x0A1fit[index][0],
		'y0A1fit' : y0A1fit[index][0],
		'x0A3fit' : x0A3fit[index][0],
		'y0A3fit' : y0A3fit[index][0],
		'a' : a[index][0],
		'b' : b[index],
		'PAdeg' : PAdeg[index][0],
		'InFit1D' : InFit1D[index][0],
		'RnFit1D' : RnFit1D[index][0],
		'nFit1D' : nFit1D[index][0],
		'xsin' : xsin[index][0],
		'x0Fit2D' : x0Fit2D[index][0],
		'y0Fit2D' : y0Fit2D[index][0],
		'InFit2D' : InFit2D[index][0],
		'RnFit2D' : RnFit2D[index][0],
		'nFit2D' : nFit2D[index][0],
		'qFit2D' : qFit2D[index][0],
		'PAFit2D' : PAFit2D[index][0],
		'Rp' : Rp[index][0],
		'C1' : C1[index][0],
		'C2' : C2[index][0],
		'R20' : R20[index][0],
		'R50' : R50[index][0],
		'R80' : R80[index][0],
		'R90' : R90[index][0],
		'A1' : A1[index][0],
		'A2' : A2[index][0],
		'A3' : A3[index][0],
		'A4' : A4[index][0],
		'S1' : S1[index][0],
		'S3' : S3[index][0],
		'G' : G[index][0],
		'M20' : M20[index][0],
		'psi' : psi[index][0],
		'sigma_psi' : sigma_psi[index][0],
		'H' : H[index][0],
		'QF' : QF[index][0],
		'mfmtk_out' : pathMfmtk + galaxyName + '_i_mfmtk.png'
	})
	return HttpResponse(template.render(context))

"""