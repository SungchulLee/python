def f(x,y,z=3,w=4):
  print(f"{x = }, {y = }, {z = }, {w = }")

def main():
    f( 1, 2, 1, 2 )

    args = ( 1, 2, 1, 2 )
    f( *args )

    kwargs = {"x": 1,"y": 2,"z": 1,"w": 2}
    f( **kwargs )

    args = ( 1, 2 )
    kwargs = {"z": 1,"w": 2}
    f( *args, **kwargs )

if __name__ == "__main__":
    main()