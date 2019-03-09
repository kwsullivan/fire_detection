# Fire Detection Implementation and Testing

fire.py is an implementation of the histogram backprojection method for fire detection proposed by Wirth and Zaremba in their 2010 paper "Flame region detection based on histogram backprojection". The implementation uses both images used in the aformentioned paper and images selected to test this particular implementation and its drawbacks.
The following describes how to run the algorithm through tests discussed in the included paper. Please refer to the attached paper for a full dissection of testing and results.<br>Note that Make is required to execute these commands, otherwise execute them manually based on the makefile.
<br><br>**Images must be opened manually in Windows OS, they will be opened automatically in OSX.**

## Running All Tests Sequentially
<pre>
make all
</pre>
## Opening All Output Images
<pre>
make open
</pre>
## Running the Ground Truth Image Tests
### Run Tests (Windows OS & Mac OS)
<pre>
make tests
</pre>
### Open Images (Mac OS)
<pre>
make stopen
</pre>

## Running the False Positive Image Tests
### Run Tests (Windows OS & Mac OS)
<pre>
make fptests
</pre>
### Open Images (Mac OS)
<pre>
make fpopen
</pre>

## Running the False Negative Image Tests
### Run Tests (Windows OS & Mac OS)
<pre>
make chtests
</pre>
### Open Images (Mac OS)
<pre>
make chopen
</pre>

## Deleting Image Outputs
<pre>
make clean
</pre>
