param (
    [string]$Val
)

$directory = "C:\Users\USER\Desktop\adebayoomolumo.website\portfolio\projects\img\works\$Val\"
$files = Get-ChildItem $directory
$i = 1
foreach ($file in $files) {
    $baseName, $extension = $file.Name.Split(".")
    $newName = $i.ToString() + "." + $extension

    $i++
    Rename-Item ($directory + $file.Name) ($directory + $newName)
}
