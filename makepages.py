import numpy as np
import os, os.path
import shutil


names = np.array(['Kate', 'Lamia', 'Marth', 'Nala', 'Nelle', 'Nina',
                  'Petra', 'River', 'Salem', 'Vesta', 'Xena'])
namessold = np.array(['Aspen', 'Cadence', 'Cassandra', 'Coraline', 'Ivy',
                      'Lorelei', 'Spruce', 'Tourmaline'])
prices = np.array(['160€', '160€', '160€', '180€', '175€', '140€',
                   '130€', '120€', '175€', '150€', '210€'])

dimensions = np.array(['50 x 40 cm', '35 x 27 cm', '35 x 27 cm',
                       '46 x 38 cm', '46 x 38 cm', '35 x 27 cm',
                       '35 x 27 cm', '30 x 30 cm', '?? x ?? cm',
                       '35 x 27 cm', '46 x 38 cm'])

availability = np.array(['Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available'])

pics = np.array([['https://drive.google.com/uc?export=view&id=1bp_hRo-BxsNH8pjGowfI1R0ORUUBwk62','https://drive.google.com/uc?export=view&id=1udAAmIZMStAbQ3cbdQmjkDAAO0EgVqi0'],
                 ['https://drive.google.com/uc?export=view&id=1LCokJrfMiS7C3PHfy0yNRKHEwz7VUaZk','https://drive.google.com/uc?export=view&id=1RE3I6qd7W-regyaIirVgdqf9GX8pVVha'],
                 ['https://drive.google.com/uc?export=view&id=1MxiQ9AlwhPy5ufAlK2NHYQZyLy4-ElWH','https://drive.google.com/uc?export=view&id=1tJwQAS1N6UE6-sX9CUyWHFxgFkbxYBu0'],
                 ['https://drive.google.com/uc?export=view&id=1wLI8e-RlJCFSl18YGozhq0_xiQVacf0P','https://drive.google.com/uc?export=view&id=1nLZnjtyf4iEiRO71egtKhq-Jgun-VVSG'],
                 ['https://drive.google.com/uc?export=view&id=1eURWahkQTX60yS54ur54b7ZruWvpCvtl','https://drive.google.com/uc?export=view&id=1ANagJ_jj_b0VrbLJ_BDF1p6zHn84QPvy'],
                 ['https://drive.google.com/uc?export=view&id=1JPZ_xNVDdDVLhqsoqNkLBznZ3ReLeoOP','https://drive.google.com/uc?export=view&id=1EHjJLbd6R7UVnDjybaK3oPhHX6p-2Dg_'],
                 ['https://drive.google.com/uc?export=view&id=1hXwpFnJeSc_mdXDrzQAEHuBppTBmbqFF','https://drive.google.com/uc?export=view&id=1T-lUTEbFaCHhDTaFsL0gs85DdgkzbPLx'],
                 ['https://drive.google.com/uc?export=view&id=1lpRtasGKA-fFX5fFonz6WE1Rl7SpabZE','https://drive.google.com/uc?export=view&id=1sNHgx-cZMp8PsZMfSimfinQ827NJr3uK'],
                 ['https://drive.google.com/uc?export=view&id=16EJIjJkFiX7em5Ug4hgs2xuXAvBOC7V1','https://drive.google.com/uc?export=view&id=1itfd_WONZe8z660P-vWGVeNSZIiFUnJ0'],
                 ['https://drive.google.com/uc?export=view&id=1tj4sEeg7kqECcvmIiff225gSfttObO8d','https://drive.google.com/uc?export=view&id=12ZQxAknVIOY2ILi47dvNMcaWCbPYX8wh'],
                 ['https://drive.google.com/uc?export=view&id=1baug7yBC4-JkC_DlIcja_tEVYS5ixrXv','https://drive.google.com/uc?export=view&id=1Ca7SZj_OKOOObasSI-NYN_k-uB0ckHgB']])
picssold = np.array(['https://drive.google.com/uc?export=view&id=/1M_cIi65vExpKwN7y34iV5wu1walcKKI1', 
                     'https://drive.google.com/uc?export=view&id=/1neYAR3abXpzndFd1QSJ_muImxWe2pXFU',
                     'https://drive.google.com/uc?export=view&id=/1WaqIMbR0eyR0cRtoWAxZcwfHfgGuxO-s',
                     'https://drive.google.com/uc?export=view&id=/1gLjw6B3N8p9a9ApE4o1u-sa-5JqDXV-w',
                     'https://drive.google.com/uc?export=view&id=1l5or-Cy-lfPPAbFH-H_DnOPu5VsiTGS5',
                     'https://drive.google.com/uc?export=view&id=/1RsN1kdJdFQxd6el32i-HhtndCOfk67Dc',
                     'https://drive.google.com/uc?export=view&id=1VaTyE-KYRXXJR_52FXOezlvR_gIMf8dg',
                     'https://drive.google.com/uc?export=view&id=/1u0XZrTwL7lrjW4wU2K-p1C7Mbd50cPKY'])


for i in np.arange(len(names))[1:]:
#    shutil.copy('paintings/kate.html', 'paintings/'+names[i].lower()+'.html')
    with open('paintings/kate.html') as ogin:
        linelist = ogin.readlines()
    newpic1 = pics[i,0]
    linelist[27]='          <img src=\''+newpic1+'\' width=\'500\'>\n'
    newpic2 = pics[i,1]
    linelist[28]='          <img src=\''+newpic2+'\' width=\'500\'>\n'
    newname = names[i]
    linelist[31]='          <h3>'+newname+'</h3>\n'
    linelist[32]='          <h4>'+availability[i]+'</h4>\n'
    linelist[33]='          <h4>Dimensions: '+dimensions[i]+'</h4>\n'
    linelist[34]='          <h4>'+prices[i]+'</h4>\n'
    with open('paintings/'+names[i].lower()+'.html', 'w') as f:
        f.writelines(linelist)



for i in np.arange(len(namessold))[1:]:

    with open('paintings/kate.html') as og:
        lines = og.readlines()
    lines[27]='          <img src=\''+picssold[i]+'\' width=\'500\'>'+'\n'
    lines[28]=''
    lines[31]='          <h3>'+namessold[i]+'</h3>\n'
    lines[32]='          <h4>Sold</h4>\n'
    lines[33]=''
    lines[34]=''
    lines[36:46]=''

    with open('soldpaintings/'+namessold[i].lower()+'.html', 'w') as ff:
        ff.writelines(lines)


print('Program finished, painting files created')
