% Load the shared library
libraryPath = '../../build/libdice.so';  % Replace with the actual path to your library
lib = dlopen(libraryPath, 1);

% Define the function signature
returnType = 'void'; 
argTypes = {'char*', 'char*'};
roll_and_write = libpointer('string', '');

% Call the function
[param1, param2] = deal('20d8', 'output.txt'); 
calllib(lib, 'roll_and_write', roll_and_write, param1, param2);

% Unload the library
dlclose(lib);

% read result
outputFilePath = 'output.txt';  % Replace with the actual path to your output file
result = dlmread(outputFilePath);

% Check if the result is greater than 1
if result > 1
    disp('Result is greater than 1!');
    exit(0)
else
    disp('Result is not greater than 1.');
end
exit(1)
