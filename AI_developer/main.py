from flet import *


def main(page: Page):
    page.title = "Flet portfoilio"

    def on_resize(e):
        if page.width <= 730:
            navigation_bar.controls[0].visible = False
            navigation_bar.update()
        else:
            navigation_bar.controls[0].visible = True
            navigation_bar.update()


    def change_text_color(e):
        if e.control.content.color == "white":
            e.control.content.color = "#2B208E"
            e.control.content.update()
        else:
            e.control.content.color = "white"
            e.control.content.update()


    navigation_bar = Row(
        alignment="center",
        controls=[
            Container(
                padding=padding.only(left=540, top=40),
                height=90,
                content=Row(controls=[
                    Container(
                        content=TextButton(
                            content=Text("Home",
                                         size=20,
                                         weight="w600",
                                         color=colors.WHITE,
                                         font_family="Open Sans"
                                         ),
                                    on_click=change_text_color
                                     ),
                        visible=True
                            ),
                    Container(
                        content=TextButton(
                            content=Text("About",
                                         size=20,
                                         weight="w600",
                                         color=colors.WHITE,
                                         font_family="Open Sans"
                                         ),
                            on_click=change_text_color
                        ),
                        visible=True
                    ),
                    Container(
                        content=TextButton(
                            content=Text("Contact",
                                         size=20,
                                         weight="w600",
                                         color=colors.WHITE,
                                         font_family="Open Sans"),
                                on_click=change_text_color
                                    ),
                        visible=True
                    ),
                    Container(
                        content=TextButton(
                            content=Text("Services",
                                         size=20,
                                         weight="w600",
                                         color=colors.WHITE,
                                         font_family="Open Sans"),
                                on_click=change_text_color
                        ),
                        visible=True
                    ),
                    Container(
                        visible=True,
                        ink=True,
                        padding=padding.only(top=3),
                        content=ResponsiveRow(
                        expand=True,
                        width=40,
                        height=40,
                        vertical_alignment=alignment.center,
                        controls=[PopupMenuButton(
                            items=[
                                PopupMenuItem(text="About us"),
                                PopupMenuItem(text="Contact"),
                                PopupMenuItem(text="Help us")
                            ],
                        )]
                    )),
                    Container(
                        alignment=alignment.top_center,
                        padding=padding.only(left=350),
                        content=ElevatedButton(content=Text("Hire me", font_family="Arial", weight="w600", size=18),
                                               width=150,
                                               height=70,
                                               color=colors.WHITE,
                                               bgcolor="#2B208E",
                                               style=ButtonStyle(shape={
                                                   MaterialState.HOVERED: RoundedRectangleBorder(radius=25),
                                                   MaterialState.DEFAULT: RoundedRectangleBorder(radius=25)
                                               }),
                                               expand=True
                                               ),
                        visible=True,
                        ink=True
                    ),
                ]), margin=margin.only(right=-5),
            )
        ]
    )


    image_now = ResponsiveRow(alignment=alignment.center,
                              controls=[
                                  Container(
                                      alignment=alignment.top_center,
                                      padding=padding.only(right=1300, top=-850),
                                      content=Image(
                                          src="logo.png",
                                          width=110,
                                          height=110
                                      ),
                                      expand=True,
                                      ink=True,
                                      visible=True
                                  )
                              ])

# title center
    title_now = ResponsiveRow(alignment=alignment.center,
                                     controls=[
                                         Container(
                                             alignment=alignment.top_center,
                                             padding=padding.only(right=1060, top=160),
                                             content=Text("CREATE YOUR STIE LIKE A PRO",
                                                 size=20,
                                                 weight="w900",
                                                 color="#30019E",
                                                 font_family="Arial"
                                             ),
                                             visible=True
                                         )
                                     ])

    title_me = ResponsiveRow(alignment=alignment.center,
                              controls=[
                                  Container(
                                      alignment=alignment.top_center,
                                      padding=padding.only(right=810, top=10),
                                      content=Text(
                                          "Hi, I'm Azizbek programmer",
                                          size=40,
                                          weight="w900",
                                          font_family="Arial",
                                          color=colors.WHITE70
                                      ),
                                      visible=True
                                  )
                              ])

    title_bottom = ResponsiveRow(alignment=alignment.center,
                                 controls=[
                                     Container(
                                         alignment=alignment.top_center,
                                         padding=padding.only(right=800, top=20, left=60),
                                         content=Text(
                                             "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Repellendus rem eos aliquid quo rerum"
                                             "temporibus ipsum distinctio numquam ut omnis placeat, nam sint atque quos dolorem laborum? Rerum, esse"
                                             "dolorem.",
                                             size=20,
                                             weight="w800",
                                             font_family="Arial"
                                         ),
                                         visible=True
                                        )
                                 ])



    image_top = ResponsiveRow(alignment=alignment.center,
                              controls=[
                                  Container(
                                      alignment=alignment.top_center,
                                      padding=padding.only(left=760, top=-630),
                                      content=Image(
                                          src="header.png",
                                          width=880,
                                          height=880
                                      ),
                                      visible=True
                                  )
                              ])

    button_now = Container(
                    alignment=alignment.top_center,
                    padding=padding.only(top=30, right=1260),
                    content=ElevatedButton(content=Text("Get started", font_family="Arial", weight="w600", size=18),
                               width=160,
                               height=55,
                               color=colors.WHITE,
                               bgcolor="#2B208E",
                               expand=True
                               ),
                visible=True
                )



    main_column = Column(horizontal_alignment="center", expand=True)
    main_column.controls.append(navigation_bar)
    main_column.controls.append(title_now)
    main_column.controls.append(title_me)
    main_column.controls.append(title_bottom)
    main_column.controls.append(button_now)
    main_column.controls.append(image_top)
    main_column.controls.append(image_now)


    background_form = Container(
        expand=True,
        height=page.height,
        margin=-10,
        gradient=LinearGradient(
            begin=alignment.bottom_right,
            end=alignment.top_left,
            colors=["#000000", "#000000","#000019", "#2B2072"]
        ),
        content=main_column,
        visible=True
    )

    page.on_resize = on_resize
    page.add(background_form)


if __name__=="__main__":
    app(target=main, view=FLET_APP)