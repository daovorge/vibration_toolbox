# Autogenerated with SMOP version 
# /Users/jslater/Library/Python/2.7/bin/smop vtb6_3.m

from __future__ import division
try:
    from runtime import *
except ImportError:
    from smop.runtime import *

def vtb6_3_(n=None,bctype=None,bmpar=None,npoints=None,*args,**kwargs):
    varargin = cellarray(args)
    nargin = 4-[n,bctype,bmpar,npoints].count(None)+len(args)

    if nargin == 3:
        npoints=100
    E=bmpar[1]
    I=bmpar[2]
    rho=bmpar[3]
    A=bmpar[4]
    L=bmpar[5]
    _len=[arange_(0,1,(1 / (npoints - 1)))].T
    if bctype == 1:
        desc=matlabarray([char('Free-Free ')])
        Bnllow=matlabarray([0,0,4.73004074486,7.8532046241,10.995607838,14.1371654913,17.2787596574])
        for i in arange_(1,length_(n)).reshape(-1):
            if n[i] > 7:
                Bnl[i]=(2 * n[i] - 3) * pi / 2
            else:
                Bnl[i]=Bnllow[n[i]]
        for i in arange_(1,length_(n)).reshape(-1):
            if n[i] == 1:
                w[i,1]=0
                U[:,i]=1 + _len * 0
            else:
                if n[i] == 2:
                    w[i,1]=0
                    U[:,i]=_len - 0.5
                else:
                    sig=(cosh_(Bnl[i]) - cos_(Bnl[i])) / (sinh_(Bnl[i]) - sin_(Bnl[i]))
                    w[i,1]=(Bnl[i] ** 2) * sqrt_(E * I / (rho * A * L ** 4))
                    b=Bnl[i] * _len
                    U[:,i]=cosh_(b) + cos_(b) - sig * (sinh_(b) + sin_(b))
    else:
        if bctype == 2:
            desc=matlabarray([char('Clamped-Free ')])
            Bnllow=matlabarray([1.88,4.69,7.85,10.99,14.14])
            for i in arange_(1,length_(n)).reshape(-1):
                if n[i] > 5:
                    Bnl[i]=(2 * n[i] - 1) * pi / 2
                else:
                    Bnl[i]=Bnllow[n[i]]
            for i in arange_(1,length_(n)).reshape(-1):
                sig=(sinh_(Bnl[i]) - sin_(Bnl[i])) / (cosh_(Bnl[i]) - cos_(Bnl[i]))
                w[i,1]=(Bnl[i] ** 2) * sqrt_(E * I / (rho * A * L ** 4))
                b=Bnl[i] * _len
                U[:,i]=cosh_(b) - cos_(b) - sig * (sinh_(b) - sin_(b))
        else:
            if bctype == 3:
                desc=matlabarray([char('Clamped-Pinned ')])
                Bnllow=matlabarray([3.93,7.07,10.21,13.35,16.49])
                for i in arange_(1,length_(n)).reshape(-1):
                    if n[i] > 5:
                        Bnl[i]=(4 * n[i] + 1) * pi / 4
                    else:
                        Bnl[i]=Bnllow[n[i]]
                for i in arange_(1,length_(n)).reshape(-1):
                    sig=(cosh_(Bnl[i]) - cos_(Bnl[i])) / (sinh_(Bnl[i]) - sin_(Bnl[i]))
                    w[i,1]=(Bnl[i] ** 2) * sqrt_(E * I / (rho * A * L ** 4))
                    b=Bnl[i] * _len
                    U[:,i]=cosh_(b) - cos_(b) - sig * (sinh_(b) - sin_(b))
            else:
                if bctype == 4:
                    desc=matlabarray([char('Clamped-Sliding ')])
                    Bnllow=matlabarray([2.37,5.5,8.64,11.78,14.92])
                    for i in arange_(1,length_(n)).reshape(-1):
                        if n[i] > 5:
                            Bnl[i]=(4 * n[i] - 1) * pi / 4
                        else:
                            Bnl[i]=Bnllow[n[i]]
                    for i in arange_(1,length_(n)).reshape(-1):
                        sig=(sinh_(Bnl[i]) + sin_(Bnl[i])) / (cosh_(Bnl[i]) - cos_(Bnl[i]))
                        w[i,1]=(Bnl[i] ** 2) * sqrt_(E * I / (rho * A * L ** 4))
                        b=Bnl[i] * _len
                        U[:,i]=cosh_(b) - cos_(b) - sig * (sinh_(b) - sin_(b))
                else:
                    if bctype == 5:
                        desc=matlabarray([char('Clamped-Clamped')])
                        Bnllow=matlabarray([4.73,7.85,11,14.14,17.28])
                        for i in arange_(1,length_(n)).reshape(-1):
                            if n[i] > 5:
                                Bnl[i]=(2 * n[i] + 1) * pi / 2
                            else:
                                Bnl[i]=Bnllow[n[i]]
                        for i in arange_(1,length_(n)).reshape(-1):
                            sig=(cosh_(Bnl[i]) - cos_(Bnl[i])) / (sinh_(Bnl[i]) - sin_(Bnl[i]))
                            w[i,1]=(Bnl[i] ** 2) * sqrt_(E * I / (rho * A * L ** 4))
                            b=Bnl[i] * _len
                            U[:,i]=cosh_(b) - cos_(b) - sig * (sinh_(b) - sin_(b))
                    else:
                        if bctype == 6:
                            desc=matlabarray([char('Pinned-Pinned')])
                            for i in arange_(1,length_(n)).reshape(-1):
                                Bnl[i]=n[i] * pi
                                w[i,1]=(Bnl[i] ** 2) * sqrt_(E * I / (rho * A * L ** 4))
                                U[:,i]=sin_(Bnl[i] * _len)
    for i in arange_(1,length_(n)).reshape(-1):
        U[:,i]=U[:,i] / sqrt_(U[:,i].T * U[:,i] * rho * A * L)
    global stopstop,ppause
    ppause=0
    x=_len * L
    if nargout == 0:
        if length_(n) != 1:
            for i in arange_(1,length_(n)).reshape(-1):
                plot_(x,U[:,i])
                axis_([0,L,min_(min_(U)),max_(max_(U))])
                figure_(gcf)
                title_([desc,char('  '),char('Mode '),int2str_(i),char('     Natural Frequency = '),num2str_(w[i]),char(' rad/s')])
                ylabel_(char('Modal Amplitude'))
                xlabel_(char('Length along bar - x'))
                grid_(char('on'))
                disp_(char('Press return to continue'))
                pause
        else:
            nsteps=50
            clf
            step=2 * pi / (nsteps)
            i=arange_(0,(2 * pi - step),step)
            hold_(char('off'))
            handle=uicontrol_(char('style'),char('pushbutton'),char('units'),char('normal'),char('backgroundcolor'),char('red'),char('position'),[0.94,0.94,0.05,0.05],char('String'),char('Stop'),char('callback'),char('global stopstop;stopstop=1;'))
            handle2=uicontrol_(char('style'),char('pushbutton'),char('units'),char('normal'),char('backgroundcolor'),char('yellow'),char('position'),[0.94,0.87,0.05,0.05],char('String'),char('Pause'),char('callback'),char('global ppause;ppause=1;'))
            handle3=uicontrol_(char('style'),char('pushbutton'),char('units'),char('normal'),char('backgroundcolor'),char('green'),char('position'),[0.94,0.8,0.05,0.05],char('String'),char('Resume'),char('callback'),char('global ppause;ppause=0;'))
            stopstop=0
            bb=0
            while stopstop == 0 and bb < 100:

                bb=bb + 1
                for ii in [i].reshape(-1):
                    while ppause == 1:

                        pause_(0.01)
                        if stopstop == 1:
                            delete_(handle)
                            delete_(handle2)
                            delete_(handle3)
                            return w,x,U

                    plot_(x,U[:,1] * cos_(ii))
                    axis_([0,L,- max_(abs_(U)),max_(abs_(U))])
                    grid_(char('on'))
                    figure_(gcf)
                    title_([desc,char('  '),char('Mode '),int2str_(n),char('     \\omega_n = '),num2str_(w[1]),char(' rad/s')])
                    ylabel_(char('Modal Amplitude'))
                    xlabel_(char('Length along bar - x'))
                    drawnow

            clear_(char('stopstop'))
            delete_(handle)
            delete_(handle2)
            delete_(handle3)
    vtbchk
    return w,x,U