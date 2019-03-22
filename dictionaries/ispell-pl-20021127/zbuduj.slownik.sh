#!/bin/bash

#
# autor:Miroslaw.Prywata@fuw.edu.pl
#
# Skrypt tworz±cy automatycznie s³ownik dla ispella 
# wersja: 20021127
#


JEZ=polish
SL_DIC=$JEZ.dic
TMPDIC=$SL_DIC.tmp

[ -f $SL_DIC ] && rm $SL_DIC

echo S³ownik: zawiera
for i in `grep "^X" slowniki.cfg | cut -f2`; do
 [ -f $i ] && ( echo $i ; cat $i >> $TMPDIC )
 [ -f fachowe/$i ] && ( echo "fachowy:$i"; cat fachowe/$i >> $TMPDIC )
done

sort +1 -nr $TMPDIC | cut -f1 > $SL_DIC && rm $TMPDIC
buildhash $SL_DIC $JEZ.aff $JEZ.hash && rm -f $SL_DIC $SL_DIC.{cnt,stat}