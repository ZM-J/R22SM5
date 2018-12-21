# R2 2 SM5
This is a simple Python script which can transform a R2Beat-style note (XML file) to a corresponding [Pump-It-Up](www.piugame.com)-style [Stepmania 5](www.stepmania.com) (SM file) note.

## Special attention

Official R2Beat notes use `encoding="euc-kr"` in XML head as default, which cannot be accepted by this script. Change it to `encoding="utf-8"` manually beforehand.

## Limitations

1. This simple script cannot deal with those R2Beat steps containing key sound effect. Key sound effect will be ignored.

2. This simple script does not set descriptive information about the song, including `ARTIST`, `BACKGROUND`, `BANNER`, `SAMPLESTART`, `SAMPLELENGTH`, difficulty information of the note, etc., due to the information limitations in R2Beat XML file. This work should be done manually after transformation.

3. This simple script does not consider SPECIAL obstacle types in R2Beat (which is not included in R2Beat CN Server) containing `up & down` (Kind="33" in XML attribute), `left & right kind#1` (Kind="33" in XML attribute), and `left & right kind#2` (Kind="34" in XML attribute). These kinds of obstacles will be ignored.

4. This simple script just does a simple transformation, and the result note will be tough in step manners. Refinement after transformation by human is crucial.