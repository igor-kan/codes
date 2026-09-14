; ModuleID = 'algorithms/02_c/sorting/selection_sort.c'
source_filename = "algorithms/02_c/sorting/selection_sort.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@__const.main.data = private unnamed_addr constant [10 x i32] [i32 33, i32 7, i32 91, i32 12, i32 5, i32 5, i32 78, i32 2, i32 44, i32 19], align 16
@.str = private unnamed_addr constant [50 x i8] c"[C SelectionSort] FAILED: not sorted at index %d\0A\00", align 1
@.str.1 = private unnamed_addr constant [45 x i8] c"[C SelectionSort] Selection sort verified: {\00", align 1
@.str.2 = private unnamed_addr constant [5 x i8] c"%d%s\00", align 1
@.str.3 = private unnamed_addr constant [3 x i8] c", \00", align 1
@.str.4 = private unnamed_addr constant [3 x i8] c"}\0A\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @selection_sort(ptr noundef captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = icmp sgt i32 %1, 1
  br i1 %3, label %4, label %9

4:                                                ; preds = %2
  %5 = add nsw i32 %1, -1
  %6 = zext nneg i32 %5 to i64
  %7 = zext nneg i32 %1 to i64
  %8 = add nsw i64 %7, -2
  br label %10

9:                                                ; preds = %40, %2
  ret void

10:                                               ; preds = %40, %4
  %11 = phi i64 [ 0, %4 ], [ %16, %40 ]
  %12 = phi i64 [ 1, %4 ], [ %47, %40 ]
  %13 = xor i64 %11, -1
  %14 = add nsw i64 %13, %7
  %15 = sub i64 %8, %11
  %16 = add nuw nsw i64 %11, 1
  %17 = trunc nuw nsw i64 %11 to i32
  %18 = and i64 %14, 3
  %19 = icmp eq i64 %18, 0
  br i1 %19, label %35, label %20

20:                                               ; preds = %10, %20
  %21 = phi i64 [ %32, %20 ], [ %12, %10 ]
  %22 = phi i32 [ %31, %20 ], [ %17, %10 ]
  %23 = phi i64 [ %33, %20 ], [ 0, %10 ]
  %24 = getelementptr inbounds nuw i32, ptr %0, i64 %21
  %25 = load i32, ptr %24, align 4, !tbaa !5
  %26 = sext i32 %22 to i64
  %27 = getelementptr inbounds i32, ptr %0, i64 %26
  %28 = load i32, ptr %27, align 4, !tbaa !5
  %29 = icmp slt i32 %25, %28
  %30 = trunc nuw nsw i64 %21 to i32
  %31 = select i1 %29, i32 %30, i32 %22
  %32 = add nuw nsw i64 %21, 1
  %33 = add i64 %23, 1
  %34 = icmp eq i64 %33, %18
  br i1 %34, label %35, label %20, !llvm.loop !9

35:                                               ; preds = %20, %10
  %36 = phi i32 [ poison, %10 ], [ %31, %20 ]
  %37 = phi i64 [ %12, %10 ], [ %32, %20 ]
  %38 = phi i32 [ %17, %10 ], [ %31, %20 ]
  %39 = icmp ult i64 %15, 3
  br i1 %39, label %40, label %49

40:                                               ; preds = %49, %35
  %41 = phi i32 [ %36, %35 ], [ %86, %49 ]
  %42 = getelementptr inbounds nuw i32, ptr %0, i64 %11
  %43 = load i32, ptr %42, align 4, !tbaa !5
  %44 = sext i32 %41 to i64
  %45 = getelementptr inbounds i32, ptr %0, i64 %44
  %46 = load i32, ptr %45, align 4, !tbaa !5
  store i32 %46, ptr %42, align 4, !tbaa !5
  store i32 %43, ptr %45, align 4, !tbaa !5
  %47 = add nuw nsw i64 %12, 1
  %48 = icmp eq i64 %16, %6
  br i1 %48, label %9, label %10, !llvm.loop !11

49:                                               ; preds = %35, %49
  %50 = phi i64 [ %87, %49 ], [ %37, %35 ]
  %51 = phi i32 [ %86, %49 ], [ %38, %35 ]
  %52 = getelementptr inbounds nuw i32, ptr %0, i64 %50
  %53 = load i32, ptr %52, align 4, !tbaa !5
  %54 = sext i32 %51 to i64
  %55 = getelementptr inbounds i32, ptr %0, i64 %54
  %56 = load i32, ptr %55, align 4, !tbaa !5
  %57 = icmp slt i32 %53, %56
  %58 = trunc nuw nsw i64 %50 to i32
  %59 = select i1 %57, i32 %58, i32 %51
  %60 = add nuw nsw i64 %50, 1
  %61 = getelementptr inbounds nuw i32, ptr %0, i64 %60
  %62 = load i32, ptr %61, align 4, !tbaa !5
  %63 = sext i32 %59 to i64
  %64 = getelementptr inbounds i32, ptr %0, i64 %63
  %65 = load i32, ptr %64, align 4, !tbaa !5
  %66 = icmp slt i32 %62, %65
  %67 = trunc nuw nsw i64 %60 to i32
  %68 = select i1 %66, i32 %67, i32 %59
  %69 = add nuw nsw i64 %50, 2
  %70 = getelementptr inbounds nuw i32, ptr %0, i64 %69
  %71 = load i32, ptr %70, align 4, !tbaa !5
  %72 = sext i32 %68 to i64
  %73 = getelementptr inbounds i32, ptr %0, i64 %72
  %74 = load i32, ptr %73, align 4, !tbaa !5
  %75 = icmp slt i32 %71, %74
  %76 = trunc nuw nsw i64 %69 to i32
  %77 = select i1 %75, i32 %76, i32 %68
  %78 = add nuw nsw i64 %50, 3
  %79 = getelementptr inbounds nuw i32, ptr %0, i64 %78
  %80 = load i32, ptr %79, align 4, !tbaa !5
  %81 = sext i32 %77 to i64
  %82 = getelementptr inbounds i32, ptr %0, i64 %81
  %83 = load i32, ptr %82, align 4, !tbaa !5
  %84 = icmp slt i32 %80, %83
  %85 = trunc nuw nsw i64 %78 to i32
  %86 = select i1 %84, i32 %85, i32 %77
  %87 = add nuw nsw i64 %50, 4
  %88 = icmp eq i64 %87, %7
  br i1 %88, label %40, label %49, !llvm.loop !13
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = alloca [10 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #5
  call void @llvm.memcpy.p0.p0.i64(ptr noundef nonnull align 16 dereferenceable(40) %1, ptr noundef nonnull align 16 dereferenceable(40) @__const.main.data, i64 40, i1 false)
  br label %2

2:                                                ; preds = %30, %0
  %3 = phi i64 [ 0, %0 ], [ %32, %30 ]
  %4 = phi i64 [ 1, %0 ], [ %38, %30 ]
  %5 = sub nsw i64 1, %3
  %6 = trunc nuw nsw i64 %3 to i32
  %7 = and i64 %5, 3
  %8 = icmp eq i64 %7, 0
  br i1 %8, label %24, label %9

9:                                                ; preds = %2, %9
  %10 = phi i64 [ %21, %9 ], [ %4, %2 ]
  %11 = phi i32 [ %20, %9 ], [ %6, %2 ]
  %12 = phi i64 [ %22, %9 ], [ 0, %2 ]
  %13 = getelementptr inbounds nuw i32, ptr %1, i64 %10
  %14 = load i32, ptr %13, align 4, !tbaa !5
  %15 = sext i32 %11 to i64
  %16 = getelementptr inbounds i32, ptr %1, i64 %15
  %17 = load i32, ptr %16, align 4, !tbaa !5
  %18 = icmp slt i32 %14, %17
  %19 = trunc nuw nsw i64 %10 to i32
  %20 = select i1 %18, i32 %19, i32 %11
  %21 = add nuw nsw i64 %10, 1
  %22 = add i64 %12, 1
  %23 = icmp eq i64 %22, %7
  br i1 %23, label %24, label %9, !llvm.loop !14

24:                                               ; preds = %9, %2
  %25 = phi i32 [ poison, %2 ], [ %20, %9 ]
  %26 = phi i64 [ %4, %2 ], [ %21, %9 ]
  %27 = phi i32 [ %6, %2 ], [ %20, %9 ]
  %28 = add nsw i64 %3, -6
  %29 = icmp ult i64 %28, 3
  br i1 %29, label %30, label %45

30:                                               ; preds = %45, %24
  %31 = phi i32 [ %25, %24 ], [ %82, %45 ]
  %32 = add nuw nsw i64 %3, 1
  %33 = getelementptr inbounds nuw i32, ptr %1, i64 %3
  %34 = load i32, ptr %33, align 4, !tbaa !5
  %35 = sext i32 %31 to i64
  %36 = getelementptr inbounds i32, ptr %1, i64 %35
  %37 = load i32, ptr %36, align 4, !tbaa !5
  store i32 %37, ptr %33, align 4, !tbaa !5
  store i32 %34, ptr %36, align 4, !tbaa !5
  %38 = add nuw nsw i64 %4, 1
  %39 = icmp eq i64 %32, 9
  br i1 %39, label %40, label %2, !llvm.loop !11

40:                                               ; preds = %30
  %41 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %42 = load i32, ptr %1, align 16, !tbaa !5
  %43 = load i32, ptr %41, align 4, !tbaa !5
  %44 = icmp sgt i32 %42, %43
  br i1 %44, label %129, label %85

45:                                               ; preds = %24, %45
  %46 = phi i64 [ %83, %45 ], [ %26, %24 ]
  %47 = phi i32 [ %82, %45 ], [ %27, %24 ]
  %48 = getelementptr inbounds nuw i32, ptr %1, i64 %46
  %49 = load i32, ptr %48, align 4, !tbaa !5
  %50 = sext i32 %47 to i64
  %51 = getelementptr inbounds i32, ptr %1, i64 %50
  %52 = load i32, ptr %51, align 4, !tbaa !5
  %53 = icmp slt i32 %49, %52
  %54 = trunc nuw nsw i64 %46 to i32
  %55 = select i1 %53, i32 %54, i32 %47
  %56 = add nuw nsw i64 %46, 1
  %57 = getelementptr inbounds nuw i32, ptr %1, i64 %56
  %58 = load i32, ptr %57, align 4, !tbaa !5
  %59 = sext i32 %55 to i64
  %60 = getelementptr inbounds i32, ptr %1, i64 %59
  %61 = load i32, ptr %60, align 4, !tbaa !5
  %62 = icmp slt i32 %58, %61
  %63 = trunc nuw nsw i64 %56 to i32
  %64 = select i1 %62, i32 %63, i32 %55
  %65 = add nuw nsw i64 %46, 2
  %66 = getelementptr inbounds nuw i32, ptr %1, i64 %65
  %67 = load i32, ptr %66, align 4, !tbaa !5
  %68 = sext i32 %64 to i64
  %69 = getelementptr inbounds i32, ptr %1, i64 %68
  %70 = load i32, ptr %69, align 4, !tbaa !5
  %71 = icmp slt i32 %67, %70
  %72 = trunc nuw nsw i64 %65 to i32
  %73 = select i1 %71, i32 %72, i32 %64
  %74 = add nuw nsw i64 %46, 3
  %75 = getelementptr inbounds nuw i32, ptr %1, i64 %74
  %76 = load i32, ptr %75, align 4, !tbaa !5
  %77 = sext i32 %73 to i64
  %78 = getelementptr inbounds i32, ptr %1, i64 %77
  %79 = load i32, ptr %78, align 4, !tbaa !5
  %80 = icmp slt i32 %76, %79
  %81 = trunc nuw nsw i64 %74 to i32
  %82 = select i1 %80, i32 %81, i32 %73
  %83 = add nuw nsw i64 %46, 4
  %84 = icmp eq i64 %83, 10
  br i1 %84, label %30, label %45, !llvm.loop !13

85:                                               ; preds = %40
  %86 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %87 = load i32, ptr %86, align 8, !tbaa !5
  %88 = icmp sgt i32 %43, %87
  br i1 %88, label %129, label %89

89:                                               ; preds = %85
  %90 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %91 = load i32, ptr %90, align 4, !tbaa !5
  %92 = icmp sgt i32 %87, %91
  br i1 %92, label %129, label %93

93:                                               ; preds = %89
  %94 = getelementptr inbounds nuw i8, ptr %1, i64 16
  %95 = load i32, ptr %94, align 16, !tbaa !5
  %96 = icmp sgt i32 %91, %95
  br i1 %96, label %129, label %97

97:                                               ; preds = %93
  %98 = getelementptr inbounds nuw i8, ptr %1, i64 20
  %99 = load i32, ptr %98, align 4, !tbaa !5
  %100 = icmp sgt i32 %95, %99
  br i1 %100, label %129, label %101

101:                                              ; preds = %97
  %102 = getelementptr inbounds nuw i8, ptr %1, i64 24
  %103 = load i32, ptr %102, align 8, !tbaa !5
  %104 = icmp sgt i32 %99, %103
  br i1 %104, label %129, label %105

105:                                              ; preds = %101
  %106 = getelementptr inbounds nuw i8, ptr %1, i64 28
  %107 = load i32, ptr %106, align 4, !tbaa !5
  %108 = icmp sgt i32 %103, %107
  br i1 %108, label %129, label %109

109:                                              ; preds = %105
  %110 = getelementptr inbounds nuw i8, ptr %1, i64 32
  %111 = load i32, ptr %110, align 16, !tbaa !5
  %112 = icmp sgt i32 %107, %111
  br i1 %112, label %129, label %113

113:                                              ; preds = %109
  %114 = getelementptr inbounds nuw i8, ptr %1, i64 36
  %115 = load i32, ptr %114, align 4, !tbaa !5
  %116 = icmp sgt i32 %111, %115
  br i1 %116, label %129, label %117

117:                                              ; preds = %113
  %118 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.1)
  %119 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %42, ptr noundef nonnull @.str.3)
  %120 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %43, ptr noundef nonnull @.str.3)
  %121 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %87, ptr noundef nonnull @.str.3)
  %122 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %91, ptr noundef nonnull @.str.3)
  %123 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %95, ptr noundef nonnull @.str.3)
  %124 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %99, ptr noundef nonnull @.str.3)
  %125 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %103, ptr noundef nonnull @.str.3)
  %126 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %107, ptr noundef nonnull @.str.3)
  %127 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %111, ptr noundef nonnull @.str.3)
  %128 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %115, ptr noundef nonnull @.str.4)
  br label %132

129:                                              ; preds = %113, %109, %105, %101, %97, %93, %89, %85, %40
  %130 = phi i32 [ 1, %40 ], [ 2, %85 ], [ 3, %89 ], [ 4, %93 ], [ 5, %97 ], [ 6, %101 ], [ 7, %105 ], [ 8, %109 ], [ 9, %113 ]
  %131 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %130)
  br label %132

132:                                              ; preds = %117, %129
  %133 = phi i32 [ 1, %129 ], [ 0, %117 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #5
  ret i32 %133
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: readwrite)
declare void @llvm.memcpy.p0.p0.i64(ptr noalias writeonly captures(none), ptr noalias readonly captures(none), i64, i1 immarg) #3

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #4

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: readwrite) }
attributes #4 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #5 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.unroll.disable"}
!11 = distinct !{!11, !12}
!12 = !{!"llvm.loop.mustprogress"}
!13 = distinct !{!13, !12}
!14 = distinct !{!14, !10}
