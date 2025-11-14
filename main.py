from pyscript import display


Dance = {'Jade', 'Ashley', 'Jennifer', 'Julia', 'Bella', 'Isa'}
Science = {'Jade', 'Irene', 'Harvey', 'Julia', 'Bella', 'William'}

display(Dance & Science, target='both')
display(Dance - Science, target='dance')
display(Science - Dance, target='sci')
display(Dance ^ Science, target='one')