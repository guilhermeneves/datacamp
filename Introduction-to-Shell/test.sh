echo "Primeiro Arg $1";
echo "Segundo Arg $2";
echo "Todos os Args $@";

for arg in $@; do echo $arg; done;

for arg in $@
do
  echo $arg
done
